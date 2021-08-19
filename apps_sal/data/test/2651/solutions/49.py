(N, M) = map(int, input().split())
MOD = 10 ** 9 + 7
x = [int(c) for c in input().split()]
y = [int(c) for c in input().split()]
X = 0
Y = 0
for (i, c) in enumerate(x):
    X += i * c - (N - 1 - i) * c
    X %= MOD
for (i, c) in enumerate(y):
    Y += i * c - (M - 1 - i) * c
    Y %= MOD
print(X * Y % MOD)
