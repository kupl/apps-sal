import sys
readline = sys.stdin.readline
(H, W) = map(int, readline().split())
A = [list(map(int, readline().split())) for _ in range(H)]
B = [list(map(int, readline().split())) for _ in range(H)]
dp = [[0] * W for _ in range(H)]
X = (H + W) * 80
d = abs(A[0][0] - B[0][0])
dp[0][0] = 1 << X - d
for h in range(H):
    for (w, (a, b)) in enumerate(zip(A[h], B[h])):
        if h == w == 0:
            continue
        d = abs(a - b)
        x = 0
        if h != 0:
            x |= dp[h - 1][w] << d
            x |= dp[h - 1][w] >> d
        if w != 0:
            x |= dp[h][w - 1] << d
            x |= dp[h][w - 1] >> d
        dp[h][w] = x
bit = bin(dp[-1][-1])[2:]
can = [i - X for (i, b) in enumerate(bit[::-1]) if b == '1']
answer = min((x if x >= 0 else -x for x in can))
print(answer)
