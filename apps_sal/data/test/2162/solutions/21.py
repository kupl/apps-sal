def solve(arr):
    dp = [0, 0, 0]
    for i in arr:
        if i == 1:
            dp[1] += 1
            dp[2] += 1
        if i == 2:
            dp[1] = min(dp[0:2])
            dp[0] += 1
            dp[2] += 1
        if i == 3:
            dp[2] = min(dp)
            dp[0] += 1
            dp[1] += 1

    return min(dp)


def __starting_point():
    k1, k2, k3 = map(int, input().split(" "))
    n = k1 + k2 + k3
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))
    c = list(map(int, input().split(" ")))

    assert n == len(a) + len(b) + len(c)

    arr = [0 for _ in range(n)]
    for i in a:
        arr[i - 1] = 1
    for i in b:
        arr[i - 1] = 2
    for i in c:
        arr[i - 1] = 3
    dp = [0, 0, 0]

    print(solve(arr))
__starting_point()
