N = int(input())
X = [int(_) for _ in input().split()]
ans = 10**6
for i in range(min(X), max(X) + 1):
    p = 0
    for j in range(N):
        p += (X[j] - i)**2
    ans = min(ans, p)
print(ans)
