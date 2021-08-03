n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
d = dict()
for i in range(len(a)):
    d[a[i]] = d.get(a[i], 0) + 1
res = 0


def search(num):
    l = -1
    r = len(a)
    while r - l > 1:
        m = (l + r) // 2
        if a[m] > k:
            r = m
        else:
            l = m
    return l


for i in range(len(a)):
    k = a[i] ^ x
    tr = search(k)
    if tr > -1 and tr < len(a) and a[tr] == k:
        res += d[a[tr]]
        if a[i] == k:
            res -= 1


print(res // 2)
