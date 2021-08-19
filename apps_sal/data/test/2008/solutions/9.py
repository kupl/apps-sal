import sys
input = sys.stdin.readline
N = int(input())
X = []
for _ in range(N):
    (a, b) = list(map(int, input().split()))
    c = b - a
    X.append([a, b, c])
X = sorted(X, key=lambda x: x[2])
s = 0
for i in range(N):
    s += X[i][0] * i + X[i][1] * (N - i - 1)
print(s)
