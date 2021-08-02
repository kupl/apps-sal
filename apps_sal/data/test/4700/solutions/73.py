n, m = map(int, input().split())
h = list(map(int, input().split()))
D = dict()
for i in range(1, n + 1):
    D[i] = h[i - 1]
L = [1 for i in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    if D[a] > D[b]:
        L[b - 1] = 0
    elif D[a] == D[b]:
        L[a - 1] = 0
        L[b - 1] = 0
    else:
        L[a - 1] = 0
ans = 0
for e in L:
    ans += e
print(ans)
