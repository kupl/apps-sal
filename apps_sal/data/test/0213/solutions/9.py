m, n = map(int, input().split())
canbe = []
for i in range(0, n):
    numb, et = map(int, input().split())
    can = []
    for j in range(1, 101):
        if j * et >= numb and j * (et - 1) < numb:
            can += [j]
    canbe += [can]
    can = []
canbeat = []
for i in range(1, 101):
    est = 0
    for el in canbe:
        if i in el:
            est += 1
    if est == n:
        canbeat += [i]
ans = []
for element in canbeat:
    if m % element == 0:
        ans += [m // element]
    else:
        ans += [m // element + 1]
writ = ans[0]
tr = 0
for element in ans:
    if element != writ:
        tr = -1
if tr == -1:
    print(tr)
else:
    print(writ)
