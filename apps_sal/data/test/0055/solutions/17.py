(n, k) = map(int, input().split())
a = list(bin(n))
a = a[2:]
b = []
for i in range(100005):
    b.append(0)
l = len(a)
c = 0
for i in range(l):
    if a[i] == '1':
        b[65 - (l - i - 1)] = 1
        c += 1
        lini = 65 - (l - i - 1)
if c <= k:
    gfati = 0
    for i in range(129):
        if gfati == 1:
            break
        if c == k:
            break
        if b[i] == 0:
            continue
        else:
            if i > lini:
                lini = i
            if c + b[i] <= k:
                b[i + 1] += 2 * b[i]
                c += b[i]
                b[i] = 0
            else:
                gfati = 1
    if 1:
        for i in range(lini, 1000005, 1):
            if c == k:
                break
            if b[i] != 0:
                if c + 1 <= k:
                    b[i] -= 1
                    c += 1
                    b[i + 1] += 2
    print('Yes')
    for i in range(100005):
        if b[i] != 0:
            for j in range(b[i]):
                print(65 - i, end=' ')
else:
    print('No')
