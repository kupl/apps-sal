n, m = list(map(int, input().split()))

a, b = list(map(int, input().split()))
ar1 = [a]
ar2 = [b]

lst = [[a, b]]
for i in range(m - 1):
    lst.append(list(map(int, input().split())))

ar3 = [0, 0]
ar4 = [0, 0]
for a, b in lst:
    if len(ar1) == len(ar2) == 2:
        break
    if len(ar1) != 2 and a not in ar1 and b not in ar1:
        ar1.append(a)
        ar3 = [ar1[0], b]
    if len(ar2) != 2 and a not in ar2 and b not in ar2:
        ar2.append(a)
        ar4 = [ar2[0], b]

ans = 'NO'
flag1, flag2, flag3, flag4 = 0, 0, 0, 0
for a, b in lst:
    if a not in ar1 and b not in ar1:
        flag1 = 1
    if a not in ar2 and b not in ar2:
        flag2 = 1
    if a not in ar3 and b not in ar3:
        flag3 = 1
    if a not in ar4 and b not in ar4:
        flag4 = 1

if flag1 == 0 or flag2 == 0 or flag3 == 0 or flag4 == 0:
    ans = 'YES'
print(ans)
