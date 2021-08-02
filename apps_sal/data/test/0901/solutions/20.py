n, m = map(int, input().split())
f = 1
while m > 0:
    m -= 1
    l = list(map(int, input().split()))
    n = l[0]
    l = l[1:]
    pos = set()
    neg = set()
    for i in l:
        if i < 0:
            neg.add(i)
        else:
            pos.add(i)
    gflag = 0
    for i in pos:
        if(0 - i in neg):
            gflag = 1
            break
    for i in neg:
        if(0 - i in pos):
            gflag = 1
            break
    if(gflag == 0):
        f = 0
        break
if(f == 0):
    print('YES')
else:
    print('NO')
