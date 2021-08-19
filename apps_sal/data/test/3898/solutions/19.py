n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
l2 = []
l1 = []
i = 0
ind = a.index(0)
while ind != n:
    l1.append(a[ind])
    ind = ind + 1
while len(l1) != n:
    l1.append(a[i])
    i += 1
i = 0
l3 = []
ind = b.index(0)
while ind != n:
    l3.append(b[ind])
    ind = ind + 1
while len(l3) != n:
    l3.append(b[i])
    i += 1
i = 0
ind = l3.index(l1[1])
while ind != n:
    l2.append(l3[ind])
    ind = ind + 1
while len(l2) != n - 1:
    if l3[i] != 0:
        l2.append(l3[i])
    i += 1
if l1[1:] == l2:
    print('YES')
else:
    print('NO')
