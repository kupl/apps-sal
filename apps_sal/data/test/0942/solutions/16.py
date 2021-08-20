n = int(input())
a = [int(s) for s in input().split()]
b = [-1 for i in range(n)]
m = {}
nextnum = 1
for i in range(n):
    if b[i] == -1:
        if m.get(a[i]) and m[a[i]][1] > 0:
            b[i] = m[a[i]][0]
            m[a[i]][1] -= 1
            if m[a[i]][1] == 0:
                m.pop(a[i])
        else:
            z = n - a[i] - 1
            b[i] = nextnum
            if z:
                m[a[i]] = [nextnum, z]
            nextnum += 1
if m:
    print('Impossible')
else:
    print('Possible')
    print(*b)
