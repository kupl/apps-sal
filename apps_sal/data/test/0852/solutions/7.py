def go(n, k, l, d):
    p = [0] * (2 * k)
    for t in range(0, 2 * k):
        if t <= k:
            p[t] = t
        else:
            p[t] = 2 * k - t

    h = []
    for x in range(n):
        h_x = [0] * (2 * k)
        for t in range(0, 2 * k):
            h_x[t] = d[x] + p[t]
        h.append(h_x)

    dp = []
    for x in range(n):
        dp.append([False] * (2 * k))
    for t in range(0, 2 * k):
        if h[0][t] <= l:
            dp[0][t] = True
        else:
            dp[0][t] = False
    # print(dp)
    for x in range(1, n):
        for t in range(0, 2 * k):
            if dp[x - 1][(t - 1) % (2 * k)] and h[x - 1][(t - 1) % (2 * k)] <= l and h[x][t] <= l:
                dp[x][t] = True
        for t in range(0, 2 * k):
            if dp[x][(t - 1) % (2 * k)] and h[x][(t - 1) % (2 * k)] <= l and h[x][t] <= l:
                dp[x][t] = True

    # print(dp)
    for t in range(0, 2 * k):
        if dp[n - 1][t]:
            return True
    return False


t = int(input())
for _ in range(t):
    n, k, l = map(int, input().split())
    d = list(map(int, input().split()))

    if go(n, k, l, d):
        print("Yes")
    else:
        print("No")
