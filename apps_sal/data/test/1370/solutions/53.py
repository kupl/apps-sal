import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines


def main():
    H, W, K = list(map(int, readline().split()))
    S = [list(map(int, readline().strip())) for j in range(H)]

    white = 0
    for line in S:
        white += sum(line)

    if white <= K:
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
            y[line] = [y[line][j] + S[i][j] for j in range(W)]
            if (pattern >> i) & 1:
                line += 1

        # 各列の値を加算していく
        count = [0] * (ly + 1)
        for j in range(W):
            for i in range(line + 1):
                if y[i][j] > K:
                    impossible = True
                    break

                count[i] += y[i][j]
                if count[i] > K:
                    x += 1
                    for i in range(line + 1):
                        count[i] = y[i][j]
                    break
            if x + ly > ans or impossible:
                impossible = True
                break
        if impossible:
            x = 10**6

        ans = min(ans, x + ly)

    print(ans)


def __starting_point():
    main()


__starting_point()
