N, M = list(map(int, input().split()))
X = tuple(map(int, input().split()))
Y = tuple(map(int, input().split()))
MOD = 10 ** 9 + 7

X_sum = sum((2 * i - N + 1) * x for i, x in enumerate(X)) % MOD
Y_sum = sum((2 * i - M + 1) * y for i, y in enumerate(Y)) % MOD
print((X_sum * Y_sum % MOD))
