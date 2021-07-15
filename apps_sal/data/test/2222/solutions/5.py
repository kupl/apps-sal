n = int(input())
a = [None] + list(map(int, input().split()))
p = [None, None] + list(map(int, input().split()))

f = [[0, 0, 10 ** 9] for i in range(n + 1)]
for i in range(n, 1, -1):
    if f[i][0] == 0:
        c = x = y = 1
    else:
        c, x, y = f[i]
    w = y if a[i] else x
    f[p[i]][0] += c
    f[p[i]][1] += w
    f[p[i]][2] = min(f[p[i]][2], w)
w = f[1][2] if a[1] else f[1][1]
print(f[1][0] - w + 1)
