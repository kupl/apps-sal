(n, x) = map(int, input().split())
V = []
for i in range(x + 1):
    V.append([])
for i in range(n):
    (l, r, c) = map(int, input().split())
    if r - l + 1 <= x:
        V[r - l + 1].append([l, r, c])
for i in range(x + 1):
    V[i] = sorted(V[i])
ans = int(3000000000.0 + 7)
for i in range(x + 1):
    mn = int(3000000000.0 + 7)
    p = 0
    k = 0
    for j in range(len(V[i])):
        while k != len(V[x - i]) and V[i][j][0] > V[x - i][k][1]:
            mn = min(mn, V[x - i][k][2])
            k = k + 1
        ans = min(ans, mn + V[i][j][2])
if ans == int(3000000000.0 + 7):
    print(-1)
else:
    print(ans)
