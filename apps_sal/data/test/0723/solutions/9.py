N = int(input())
W = [0 for i in range(N)]
H = [0 for i in range(N)]

for i in range(N):
    W[i], H[i] = list(map(int, input().split()))
    if not (W[i] <= H[i]):
        W[i], H[i] = H[i], W[i]

maxw = max(W)

ans = 1e10
while maxw <= 1000:
    s = 0
    for i in range(N):
        if maxw >= H[i]:
            s += W[i]
        else:
            s += H[i]
    if ans > maxw * s:
        ans = maxw * s
    maxw += 1

print(ans)
