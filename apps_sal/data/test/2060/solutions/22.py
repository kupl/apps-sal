n = int(input())
v = {3, 7}
ps = 0
while len(v) != ps:
    nv = {i for i in v}
    for a in v:
        if a + 3 <= 100:
            nv.add(a+3)
        if a + 7 <= 100:
            nv.add(a+7)
    ps = len(v)
    v = nv
for i in range(n):
    x = int(input())
    if x in v:
        print('YES')
    else:
        print('NO')
