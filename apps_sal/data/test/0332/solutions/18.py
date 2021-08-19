(n, m) = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
b = []
flag = True
for i in range(n):
    b.append(list(map(int, input().split())))
for i in range(m + n - 1):
    cur = []
    curb = []
    for l in range(i + 1):
        try:
            cur.append(a[i - l][l])
            curb.append(b[i - l][l])
        except:
            pass
    cur.sort()
    curb.sort()
    if cur != curb:
        flag = False
if flag:
    print('YES')
else:
    print('NO')
