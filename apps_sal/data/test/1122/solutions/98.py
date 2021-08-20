def solve():
    (N, M) = list(map(int, input().split()))
    m = 0
    oddN = M
    oddN += (oddN + 1) % 2
    for i in range(oddN // 2):
        print((i + 1, oddN - i))
        m += 1
        if m == M:
            return
    for i in range(M):
        print((oddN + i + 1, M * 2 + 1 - i))
        m += 1
        if m == M:
            return


def __starting_point():
    solve()


__starting_point()
