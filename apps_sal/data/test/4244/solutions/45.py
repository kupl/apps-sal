N = int(input())
X = list(map(int, input().split()))

X_min = min(X)
X_max = max(X)

ans = float('inf')
for i in range(X_min, X_max + 1):
    d = 0
    for x in X:
        d += (x - i) ** 2
    ans = min(ans, d)

print(int(ans))
return
