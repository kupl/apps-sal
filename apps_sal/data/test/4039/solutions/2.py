(n, r) = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
pos = []
neg = []
for x in a:
    if x[1] > 0:
        pos.append(x)
    else:
        neg.append(x)
pos.sort(key=lambda k: k[0])
flg = 1
for x in pos:
    if r < x[0]:
        flg = 0
    else:
        r += x[1]
neg.sort(key=lambda k: k[0] + k[1], reverse=True)
for x in neg:
    if r < x[0]:
        flg = 0
    else:
        r += x[1]
        if r < 0:
            flg = 0
if flg == 1:
    print('YES')
else:
    print('NO')
