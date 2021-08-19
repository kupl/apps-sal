def solve(a, b, c):
    n = len(a) + len(b) + len(c)
    arr = [0] * (n + 1)
    for i in a:
        arr[i] = 0
    for i in b:
        arr[i] = 1
    for i in c:
        arr[i] = 2
    dp = [[n + 10] * (n + 1) for _ in range(3)]
    for i in range(3):
        dp[i][0] = 0
        for j in range(1, n + 1):
            dp[i][j] = dp[i][j - 1] + (arr[j] != i)
            if i:
                dp[i][j] = min(dp[i - 1][j], dp[i][j])
    return dp[2][n]


def __starting_point():
    (k1, k2, k3) = map(int, input().split(' '))
    n = k1 + k2 + k3
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    c = list(map(int, input().split(' ')))
    assert n == len(a) + len(b) + len(c)
    arr = [0 for _ in range(n)]
    for i in a:
        arr[i - 1] = 1
    for i in b:
        arr[i - 1] = 2
    for i in c:
        arr[i - 1] = 3
    dp = [0, 0, 0]
    print(solve(a, b, c))


__starting_point()
