from decimal import Decimal


def f(x):
    return int(x)


A, B, N = list(map(int, input().split()))

ans = 0
if N >= B:
    X = [1, B - 1, N]
else:
    X = [1, N]
for x in X:
    if x == B:
        culc = 0
    elif x < B:
        culc = f(A * Decimal(x / B))
    else:
        culc = f(A * Decimal(x / B)) - A * f(Decimal(x / B))

    if culc > ans:
        ans = culc

print(ans)
