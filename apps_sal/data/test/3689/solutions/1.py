import sys

n, k = sys.stdin.readline().strip().split()
n = int(n)
k = int(k)
x = sys.stdin.readline().strip()
X = [0] * n
for i in range (0, n):
    X[i] = int(x[i])
v = 0
w = 0
for i in range (0, n):
    if v == 0 and (X[i] > X[i % k]):
        v = -1
    elif v == 0 and (X[i] < X[i % k]):
        v = 1
ans = []
if v == -1:
    i = k - 1
    while X[i] == 9:
        i = i - 1
    while i < k:
        X[i] = (X[i] + 1) % 10
        i = i + 1
for i in range (0, n):
    ans.append(str(X[i % k]))
print(n)
print("".join(ans))

