
def __starting_point():
    n, t = map(int, input().split())
    A = [[0] * 11 for _ in range(11)]
    ans = 0
    A[0][0] = t
    for i in range(n):
        for j in range(i + 1):
            if A[i][j] >= 1:
                A[i + 1][j] += (A[i][j] - 1) / 2
                A[i + 1][j + 1] += (A[i][j] - 1) / 2
                A[i][j] = 1
                ans += 1
    print(ans)


__starting_point()
