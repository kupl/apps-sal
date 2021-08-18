import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
H, W, D = map(int, readline().split())
X = [(0, 0) for _ in range(H * W)]
Y = [0 for _ in range(H * W)]

for i in range(H):
    A = [int(x) - 1 for x in readline().split()]
    for j in range(W):
        X[A[j]] = (i, j)

for i in range(0, H * W - D):
    Y[i + D] = Y[i] + abs(X[i + D][0] - X[i][0]) + abs(X[i + D][1] - X[i][1])

Q = int(readline())
for _ in range(Q):
    L, R = map(int, readline().split())
    print(Y[R - 1] - Y[L - 1])
