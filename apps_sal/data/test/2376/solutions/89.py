def main():
    N, W = list(map(int, input().split()))
    l = []
    w, v = list(map(int, input().split()))
    ww = w
    dp = [[[0] * (3*N) for _ in range(N+1) ]for _ in range(N)]
    dp[0][1][0] = v
    l.append((0, v))
    for _ in range(N-1):
        w, v = list(map(int, input().split()))
        l.append((w-ww, v))
    if W < ww:
        return 0
    for i in range(1, N):
        w, v = l[i]
        for j in range(1, N+1):
            for k in range(w):
                dp[i][j][k] = dp[i-1][j][k]
            for k in range(w, 3*N):
                dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-1][k-w] + v)
    r = 0
    for i in range(N+1):
        wt = W - i * ww
        if wt < 0:
            break
        r = max(r, max(dp[-1][i][:wt+1]))
    return r
print((main()))

