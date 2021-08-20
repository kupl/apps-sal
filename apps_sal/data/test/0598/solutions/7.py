(n, x) = list(map(int, input().split()))
V = []
for i in range(x + 1):
    V.append([])
for i in range(n):
    (l, r, c) = list(map(int, input().split()))
    if r - l + 1 > x:
        continue
    V[r - l + 1].append((l, c))
for i in range(x + 1):
    V[i] = sorted(V[i], key=lambda a: a[0])
ans = int(3000000000.0 + 7)
for i in range(x + 1):
    mn = int(3000000000.0 + 7)
    k = 0
    for j in range(len(V[i])):
        while k != len(V[x - i]) and V[x - i][k][0] + (x - i) - 1 < V[i][j][0]:
            mn = min(mn, V[x - i][k][1])
            k += 1
        ans = min(ans, mn + V[i][j][1])
if ans == int(3000000000.0 + 7):
    print(-1)
else:
    print(ans)
