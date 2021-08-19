n = int(input())
i = 1
l = []
while i <= n:
    l.append(input().split())
    i += 1
a = [int(p) for p in input().split()]
i = 1


def t(l, a):
    w = min(l[a[0] - 1][0], l[a[0] - 1][1])
    del a[0]
    for p in a:
        k = min(l[p - 1][0], l[p - 1][1])
        if k > w:
            w = k
        elif max(l[p - 1][0], l[p - 1][1]) > w:
            w = max(l[p - 1][0], l[p - 1][1])
        else:
            return 'NO'
    return 'YES'


print(t(l, a))
