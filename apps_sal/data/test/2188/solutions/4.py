import sys
input = sys.stdin.readline
N = int(input())
X = []
Y = []
for i in range(N):
    (a, b) = map(int, input().split())
    if a < b:
        X.append((a, b, i + 1))
    else:
        Y.append((a, b, i + 1))
if len(Y) > len(X):
    X = sorted(Y, key=lambda x: x[0])
else:
    X = sorted(X, key=lambda x: -x[0])
print(len(X))
print(*[x[2] for x in X])
