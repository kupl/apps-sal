(n, m) = map(int, input().split())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
k = input().split()
for i in range(m):
    k[i] = int(k[i])
sum1 = sum(k)
b = []
c = [0 for i in range(m)]
flag = False
for i in range(n):
    if len(b) < sum1:
        b.append(a[i])
        c[a[i] - 1] += 1
    elif len(b) == sum1:
        if c == k:
            flag = True
        c[b[0] - 1] -= 1
        b.pop(0)
        b.append(a[i])
        c[a[i] - 1] += 1
if c == k:
    flag = True
if flag:
    print('YES')
else:
    print('NO')
