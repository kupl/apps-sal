n = int(input())
a = list(map(int, input().split()))
last = -1
cnt = 0
fx = -1
kek = 0
for i in range(0, n):
    cur = a[i]
    if last == -1:
        cnt = cnt + 1
    elif last == cur:
        cnt = cnt + 1
    else:
        if fx == -1:
            fx = cnt
        elif fx != cnt:
            kek = -1
        cnt = 1
    last = cur
if fx == -1:
    fx = cnt
elif fx != cnt:
    kek = -1
if kek == -1:
    print('NO')
else:
    print('YES')
