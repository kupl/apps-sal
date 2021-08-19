n = int(input())
a = [int(x) for x in input().split()]
h = [-1] * n
b = [(a[i], i) for i in range(n)]
b.sort(reverse=True)
for e in b:
    (num, idx) = e
    flag = True
    allNeg = True
    foundLosing = False
    foundWin = False
    for i in range(idx % num, n, num):
        if i == idx:
            continue
        if h[i] != -1:
            allNeg = False
        if h[i] == 0:
            foundLosing = True
            break
        if h[i] == 1:
            foundWin = False
    if allNeg:
        h[idx] = 0
    elif foundLosing:
        h[idx] = 1
    else:
        h[idx] = 0
for i in range(n):
    if h[i] == 0:
        print('B', end='')
    else:
        print('A', end='')
