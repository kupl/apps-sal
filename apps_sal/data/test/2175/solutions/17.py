n = int(input())
a = list(map(int, input().split()))
b = list(a)
f = [i + 1 for i in range(n)]


def getf(x):
    y = x
    while x < n and a[x] == 0:
        x = f[x]
    while y < n and a[y] == 0:
        t = f[y]
        (f[y], y) = (x, t)
    return x


m = int(input())
ans = []
for i in range(m):
    tmp = list(map(int, input().split()))
    p = tmp[1] - 1
    if tmp[0] == 1:
        x = tmp[2]
        l = []
        while p < n:
            if a[p] >= x:
                a[p] -= x
                break
            l.append(p)
            x -= a[p]
            a[p] = 0
            p = f[p]
        for x in l:
            f[x] = p
    else:
        ans.append(b[p] - a[p])
print('\n'.join(map(str, ans)))
