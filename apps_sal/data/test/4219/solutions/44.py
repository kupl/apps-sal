n = int(input())
t = [[-1] * n for _ in range(n)]
ans = 0
for i in range(n):
    a = int(input())
    for j in range(a):
        (x, y) = map(int, input().split())
        t[i][x - 1] = y
for i in range(2 ** n):
    h = [0] * n
    for j in range(n):
        if i >> j & 1:
            h[j] = 1
    f = 1
    for k in range(n):
        if h[k]:
            for l in range(n):
                if t[k][l] == -1:
                    continue
                if t[k][l] != h[l]:
                    f = 0
    if f:
        ans = max(ans, h.count(1))
print(ans)
