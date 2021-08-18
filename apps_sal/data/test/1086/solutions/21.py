import sys
INF = float("inf")


def solve(H: int, W: int, A: "List[List[int]]", B: "List[List[int]]"):
    base = [[abs(A[h][w] - B[h][w]) for w in range(W)] for h in range(H)]
    mx = (1 << 12800) - 1
    table = [[0] * W for _ in range(H)]
    table[0][0] = (1 << (6400 + base[0][0])) | (1 << (6400 - base[0][0]))
    for h in range(H):
        for w in range(W):
            if h > 0:
                table[h][w] |= (table[h - 1][w] << base[h][w])
                table[h][w] |= (table[h - 1][w] >> base[h][w])
            if w > 0:
                table[h][w] |= (table[h][w - 1] << base[h][w])
                table[h][w] |= (table[h][w - 1] >> base[h][w])
            table[h][w] &= mx

    m = INF
    for j in range(12800):
        i = (table[H - 1][W - 1] >> j) & 1
        if i == 1:
            m = min(m, abs(j - 6400))
    print(m)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))
    W = int(next(tokens))
    A = [[int(next(tokens)) for _ in range(W)]
         for _ in range(H)]
    B = [[int(next(tokens)) for _ in range(W)]
         for _ in range(H)]
    solve(H, W, A, B)


def __starting_point():
    main()


__starting_point()
