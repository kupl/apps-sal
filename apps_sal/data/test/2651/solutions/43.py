MOD = 10**9 + 7
n, m = list(map(int, input().split()))
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
X.sort()
Y.sort()
xx, yy = 0, 0
for i in range(n):
    xx += X[i] * i
    xx -= X[i] * (n - i - 1)
for i in range(m):
    yy += Y[i] * i
    yy -= Y[i] * (m - i - 1)
print((xx * yy % MOD))
