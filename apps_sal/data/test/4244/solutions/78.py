N = int(input())
X = list(map(int, input().split()))
X.sort()

ans = 10**1000
for p in range(X[0], X[-1] + 1):
    tmp = 0
    for x in X:
        tmp += (x - p)**2
    ans = min(ans, tmp)
print(ans)
