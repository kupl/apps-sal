

def solve(choco, cut_pos, k):
    cuts = len(cut_pos) - 2
    blocks = [0] * (len(cut_pos) - 1)

    for col in zip(*choco):
        need_cut = False
        for i, blk in enumerate(zip(cut_pos, cut_pos[1:])):
            s, e = blk
            white = sum(col[s:e])

            if white > k:
                return float('inf')

            if blocks[i] + white > k:
                need_cut = True
                break
            else:
                blocks[i] += white

        if need_cut:
            for i, blk in enumerate(zip(cut_pos, cut_pos[1:])):
                s, e = blk
                blocks[i] = sum(col[s:e])

        cuts += need_cut
    return cuts


def main():
    h, w, k = list(map(int, input().split()))

    choco = [[int(s) for s in list(input())] for _ in range(h)]
    min_cuts = float('inf')

    for cuts in range(1 << (h - 1)):
        cut_pos = [0] + [i + 1 for i in range(h - 1) if cuts & (1 << i)] + [h]
        min_cuts = min(min_cuts, solve(choco, cut_pos, k))

    print(min_cuts)


def __starting_point():
    main()


__starting_point()
