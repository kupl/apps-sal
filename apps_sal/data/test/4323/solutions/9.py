n, m = map(int, input().split())
inf = 0
szhat = [0] * n
for i in range(n):
    a, b = map(int, input().split())
    inf += a
    szhat[i] = (a - b)
szhat.sort()
p = [0] * (n + 1)
for i in range(1, n + 1):
    p[i] = p[i - 1] + szhat[-i]
if inf - p[n] > m:
    print(-1)
else:
    L, R = -1, n
    while R - L > 1:
        med = (R + L) // 2
        if inf - p[med] > m:
            L = med
        else:
            R = med
    print(R)
