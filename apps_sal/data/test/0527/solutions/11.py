def main():
    from bisect import bisect_left

    S = input()
    T = input()

    L = len(S)

    pos = tuple(list() for _ in range(26))
    orda = ord('a')
    for i, c in enumerate(S):
        j = ord(c) - orda
        pos[j].append(i)

    rep = 0
    curr = 0
    for c in T:
        j = ord(c) - orda

        if not pos[j]:
            print((-1))
            return

        i = bisect_left(pos[j], curr)
        if i == len(pos[j]):
            rep += 1
            i = 0  # pos[j][0]文字目がc
        curr = pos[j][i] + 1  # pos[j][i]にしたら同じ文字が続くケースでWA

    print((rep * L + curr))


def __starting_point():
    main()

__starting_point()
