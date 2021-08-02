n, m = map(int, input().split())
a = input()
b = input()
c = []
d = [0] * n
c = [i for i in range(n) if a[i] == b[i]]
l = len(c)
for i in range(min(l, n - m)):
    d[c[i]] = a[c[i]]
if l < n - m:
    u = n - m - l
    if l + u + u > n:
        print(-1)
        return
    else:
        u = n - m - l
        for i in range(n):
            if d[i] == 0 and u > 0:
                d[i] = a[i]
                u -= 1
                if u == 0: break
        u = n - m - l
        for i in range(n):
            if d[i] == 0 and u > 0:
                d[i] = b[i]
                u -= 1
                if u == 0: break
for i in range(n):
    if d[i] == 0:
        for e in ['a', 'b', 'c']:
            if e != a[i] and e != b[i]:
                print(e, end='')
                break
    else:
        print(d[i], end='')
