import sys

H, W, D = map(int, sys.stdin.readline().split())
num = {}
for j in range(H):
    tmp = map(int, sys.stdin.readline().split())
    for i, n in enumerate(tmp):
        num[n] = (i, j)

# Dで分類した累積和
# S[initial % D][j], n = r + D*j
S = [0 for _ in range(H*W+D)]
for i in range(D+1, H*W+1):
    x, y = num[i]
    a, b = num[i-D]
    S[i] = S[i-D] + abs(x - a) + abs(y - b)
# print(S)
Q = int(sys.stdin.readline())
for _ in range(Q):
    L, R = map(int, sys.stdin.readline().split())
    r = L % D
    print(S[R] - S[L])
