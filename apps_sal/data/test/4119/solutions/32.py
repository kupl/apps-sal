N, M = map(int, input().split())
X = list(map(int, input().split()))
if N >= M:
    print(0)
    return
X.sort()
a = []
for i in range(M - 1):
    a.append(abs(X[i] - X[i + 1]))
a.sort()
ans = 0
for i in range(M - N):
    ans += a[i]
print(ans)
