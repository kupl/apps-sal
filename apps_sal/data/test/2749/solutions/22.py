from numpy import *
(H, W) = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))
B = []
ans = zeros((H, W), int64)
for n in range(N):
    B.extend(A[n] * [n + 1])
n = 0
for h in range(H):
    for w in range(W):
        if h % 2 == 0:
            ans[h][w] = B[n]
        else:
            ans[h][-(w + 1)] = B[n]
        n += 1
for h in range(H):
    print(*ans[h])
