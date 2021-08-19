n = int(input())
a = [n - int(x) for x in input().split()]
b = [0] * n
fh = 1
i = 0
hd = dict()
while i < n:
    if a[i] == 1:
        b[i] = fh
        fh += 1
    elif a[i] in hd:
        b[i] = hd[a[i]][0]
        hd[a[i]][1] -= 1
        if hd[a[i]][1] == 0:
            del hd[a[i]]
    else:
        b[i] = fh
        hd[a[i]] = [fh, a[i] - 1]
        fh += 1
    i += 1
if len(hd) != 0:
    print('Impossible')
else:
    print('Possible')
    print(*b)
