def tabe(a, b):
    i = 0
    while i < len(a):
        if b == a[i]:
            return i
        i = i + 1
    return -1


a = int(input())
l = []
ll = []
i = 0
while i < a:
    b = list(input().split())
    c = b[0]
    d = b[1]
    x = tabe(ll, c)
    if x == -1:
        l.append(c)
        ll.append(d)
    else:
        ll[x] = d
    i = i + 1
i = 0
print(len(l))
while i < len(l):
    print(l[i], ll[i])
    i = i + 1
