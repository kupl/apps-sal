import itertools


def main():
    H, W, K = list(map(int, input().split(' ')))
    S = [input() for _ in range(H)]
    ans = (H - 1) * (W - 1)
    for h_divs in itertools.product([0, 1], repeat=H - 1):
        h_patterns = [0] * H
        for h in range(1, H):
            h_patterns[h] = h_patterns[h - 1] + h_divs[h - 1]
        div_cnt = h_patterns[-1]
        white_cnt = [0] * (div_cnt + 1)
        valid_div = True
        for w in range(W):
            new_white_cnt = [0] * (div_cnt + 1)
            for h in range(H):
                if S[h][w] == '1':
                    new_white_cnt[h_patterns[h]] += 1
            if max(new_white_cnt) > K:
                valid_div = False
                break
            should_div = False
            for r in range(len(white_cnt)):
                if white_cnt[r] + new_white_cnt[r] > K:
                    should_div = True
                    break
            if should_div:
                div_cnt += 1
                for r in range(len(white_cnt)):
                    white_cnt[r] = new_white_cnt[r]
            else:
                for r in range(len(white_cnt)):
                    white_cnt[r] += new_white_cnt[r]
        if valid_div:
            ans = min(ans, div_cnt)
    print(ans)


def __starting_point():
    main()


__starting_point()
