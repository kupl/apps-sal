n, s = list(map(int, input().split(" ")))
a = []
aa = []
aaa = []
for x in range(n):
    q, qq = list(map(int, input().split(" ")))
    if qq > 0 and s > q:
        a.append(qq)
    aaa.append(qq)
    aa.append(float(q + float(qq / 100)))
    pass

if s < min(aa):
    print(-1)
else:
    if len(a) == 0:
        print(0)
        pass
    else:
        print(100 - min(a))
    pass
