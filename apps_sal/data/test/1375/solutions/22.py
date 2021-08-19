def solve2(n, c):
    dp = [0 for _ in range(n)]
    r = 0
    p = 0
    for i in range(n):
        dp[i] = c[i] + dp[i - 1] if i > 0 else c[i]
    t = dp[n - 1] // 3
    if t * 3 != dp[n - 1]:
        return 0
    for i in range(n - 1):
        if dp[i] == 2 * t:
            r += p
        if dp[i] == t:
            p += 1
    return r


def __starting_point():
    num_el = int(input())
    values = list(map(int, input().split()))
    print(solve2(num_el, values))


__starting_point()
