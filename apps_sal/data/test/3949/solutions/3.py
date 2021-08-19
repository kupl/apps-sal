from sys import stdin
input = stdin.readline
r, c = list(map(int, input().split()))
mat = [list(input()) for i in range(r)]
dasie = True
wiersze = []
zerow = 0
zerok = 0
for i in range(r):
    st = -1
    kon = -1
    hasze = 0
    for j in range(c):
        if mat[i][j] == '#':
            hasze += 1
            if st == -1:
                st = j
            kon = j
    wiersze.append([st, kon])
    if hasze == 0:
        zerow += 1
    if hasze != 0 and hasze != kon - st + 1:
        dasie = False
for j in range(c):
    st = -1
    kon = -1
    hasze = 0
    for i in range(r):
        if mat[i][j] == '#':
            hasze += 1
            if st == -1:
                st = i
            kon = i
    if hasze == 0:
        zerok += 1
    if hasze != 0 and hasze != kon - st + 1:
        dasie = False
if not dasie:
    print(-1)
else:
    wyn = 0
    wiersze = [[-1, -1]] + wiersze
    for i in range(1, r + 1):
        nad = wiersze[i - 1]
        pod = wiersze[i]
        if pod != [-1, -1] and nad[0] > pod[1] or nad[1] < pod[0]:
            wyn += 1
    if (zerok == 0 and zerow > 0) or (zerow == 0 and zerok > 0):
        print(-1)
    else:
        print(wyn)
