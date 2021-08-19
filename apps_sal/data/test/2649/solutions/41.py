import sys
readline = sys.stdin.readline
N = int(readline())
(X, Y) = ([None] * N, [None] * N)
for i in range(N):
    (x, y) = list(map(int, readline().split()))
    (X[i], Y[i]) = (x + y, x - y)
print(max(abs(max(X) - min(X)), abs(max(Y) - min(Y))))
