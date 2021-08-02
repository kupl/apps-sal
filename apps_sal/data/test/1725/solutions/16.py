n, m, d = map(int, input().split())
a = []
for i in range(n):
    a.extend(list(map(int, input().split())))
a.sort()
k = 0
mi = (n * m) // 2
for i in range(n * m):
    if abs(a[mi] - a[i]) % d != 0:
        print(-1)
        return
    else:
        k += (abs(a[mi] - a[i]) // d)
print(k)
