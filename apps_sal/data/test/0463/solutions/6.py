(n, m) = list(map(int, input().split()))
l = list(map(int, input().split()))
d = {}
ansz = 0
for i in l:
    if i in d:
        ansz = 1
    else:
        d[i] = 1
lz = []
ans1 = 0
for i in l:
    lz.append(i & m)
    if i & m in d and i & m != i:
        ans1 = 1
ans2 = 0
dz = {}
for i in lz:
    if i in dz:
        ans2 = 1
    else:
        dz[i] = 1
if ansz:
    print(0)
elif ans1:
    print(1)
elif ans2:
    print(2)
else:
    print(-1)
