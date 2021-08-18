n, m = list(map(int, input().split()))

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

b = []
for i in range(n):
    b.append(list(map(int, input().split())))

for i in range(m + n - 1):
    d1 = {}
    d2 = {}

    for j in range(n):
        l = j
        r = i - j
        if l >= 0 and l < n and r >= 0 and r < m:
            e = a[l][r]
            if e not in d1:
                d1[e] = 0
            d1[e] += 1

    for j in range(n):
        l = j
        r = i - j
        if l >= 0 and l < n and r >= 0 and r < m:
            e = b[l][r]
            if e not in d2:
                d2[e] = 0
            d2[e] += 1

    for k in d1:
        if k not in d2:
            print('NO')
            return
        if d1[k] != d2[k]:
            print('NO')
            return
print('YES')
