(N, M, X) = map(int, input().split())
A = list(map(int, input().split()))
X_high = 0
X_low = 0
for i in range(X, N + 1):
    if i in A:
        X_high += 1
for i in range(0, X + 1):
    if i in A:
        X_low += 1
print(min(X_high, X_low))
