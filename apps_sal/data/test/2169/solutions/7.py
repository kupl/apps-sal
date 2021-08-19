(H, W, D) = map(int, input().split())
A = [-1] * (H * W + 1)
cnt = 0
for i in range(H):
    for j in list(map(int, input().split())):
        A[j] = cnt
        cnt += 1
dp = [0] * (H * W + 1)
tmp = 1
for i in range(D):
    (h, w) = (A[tmp] // W + 1, A[tmp] % W + 1)
    t = tmp + D
    cnt = 0
    while t <= H * W:
        (x, y) = (A[t] // W + 1, A[t] % W + 1)
        cnt += abs(x - h) + abs(y - w)
        dp[t] = cnt
        (h, w) = (x, y)
        t += D
    tmp += 1
Q = int(input())
for i in range(Q):
    (l, r) = map(int, input().split())
    ans = dp[r] - dp[l]
    print(ans)
