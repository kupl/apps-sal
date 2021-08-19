(n, k) = [int(x) for x in input().strip().split(' ')]
a = [int(x) for x in input().strip().split(' ')]
d = {}
c = {}
flag = False
b = []
for i in range(n):
    if a[i] in d:
        d[a[i]].append(i)
        c[a[i]] += 1
    else:
        d[a[i]] = [i]
        c[a[i]] = 1
    b.append(0)
    if c[a[i]] > k:
        flag = True
        break
if flag:
    print('NO')
else:
    print('YES')
    cur = 0
    for j in d:
        for i in d[j]:
            b[i] = cur % k + 1
            cur += 1
    for i in range(n):
        print(b[i], end=' ')
    print()
