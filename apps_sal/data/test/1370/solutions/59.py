import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines


def main():
    H, W, K = list(map(int, readline().split()))
    S = [readline().strip() for j in range(H)]

    white = []
    for line in S:
        white.append(line.count("1"))
    white_total = sum(white)

    if white_total <= K:
        print((0))
        return

    # 横線の決め方を全探索
    ans = 10**5
    for pattern in range(2**(H - 1)):
        # 初期化
        impossible = False
        x = 0
        ly = bin(pattern).count("1")
        y = [[0] * W] * (ly + 1)
        line = 0
        for i in range(H):
            y[line] = [y[line][j] + int(S[i][j]) for j in range(W)]
            if (pattern >> i) & 1:
                line += 1

        # 各列の値を加算していく
        count = [0] * (ly + 1)
        for col in zip(*y):
            # Kより大きい値を加算する場合は不成立
            if any(a > K for a in col):
                impossible = True
                break
            for i, a in enumerate(col):
                count[i] += a
                # 和がKより大きければカット数を増やす
                if count[i] > K:
                    x += 1
                    count = list(col)
                    break
            if x + ly > ans:
                impossible = True
                break
        if impossible:
            x = 10**6

        ans = min(ans, x + ly)

    print(ans)


def __starting_point():
    main()


__starting_point()
