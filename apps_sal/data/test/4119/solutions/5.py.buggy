n, m = list(map(int, input().split()))
X = list(map(int, input().split()))

if m == 1:
    print((0))
    return

X.sort()
D = []
for i in range(1, m):
    D.append(X[i] - X[i - 1])

D.sort(reverse=True)
d = 0
if i > 1:
    for i in range(min(n - 1, m - 1)):
        d += D[i]

ans = sum(D) - d
print(ans)
