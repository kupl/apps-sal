n = int(input())
a = list(map(int, input().split()))
v = list()
last, cnt = a[0], 0
for i in range(n):
    if a[i] == last:
        cnt += 1
    else:
        v.append(cnt)
        cnt = 1
        last = a[i]
v.append(cnt)

f = True
for e in v:
    if e != v[0]:
        f = False

if (f):
    print('YES')
else:
    print('NO')
