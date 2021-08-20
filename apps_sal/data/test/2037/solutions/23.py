(n, m) = map(int, input().split())
a = list(map(int, input().split()))
b = dict()
for i in range(len(a)):
    b[a[i]] = b.get(a[i], 0)
    b[a[i]] += 1
    if len(b) == n:
        print('1', end='')
        c = []
        for k in b:
            b[k] -= 1
            if b[k] == 0:
                c.append(k)
        for j in range(len(c)):
            del b[c[j]]
    else:
        print('0', end='')
