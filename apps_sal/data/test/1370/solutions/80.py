from itertools import product

H, W, K = map(int, input().split())
l = [[0] * W for _ in range(H)]
for i in range(H):
    for j, s in enumerate(input()):
        if s == "1":
            l[i][j] = 1

dp = [[0] * (W + 1) for _ in range(H + 1)]
for i in range(1, H + 1):
    for j in range(1, W + 1):
        dp[i][j] = l[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]


def f(lx, ly, rx, ry): return dp[ry][rx] - dp[ly - 1][rx] - dp[ry][lx - 1] + dp[ly - 1][lx - 1]


ans = H * W
for i in product(range(2), repeat=H - 1):
    candidate = []
    if any(i):
        start = 1
        for j, k in enumerate(i, start=1):
            if k:
                candidate.append((start, j))
                start = j + 1
        candidate.append((start, H))
    else:
        candidate.append((1, H))

    q = [1]
    cutx = 0

    while q:
        s = q.pop()
        for t in range(s, W + 1)[::-1]:
            if all(f(s, j, t, k) <= K for j, k in candidate):
                if t != W:
                    q.append(t + 1)
                    cutx += 1
                break
        else:
            cutx = H * W
    v = cutx + sum(i)
    ans = min(ans, v)

print(ans)
