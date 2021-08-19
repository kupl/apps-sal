import sys
I = [0 for i in range(10 ** 5 + 1)]
(y2, y4, y6, y8) = (0, 0, 0, 0)
n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
for i in range(0, n):
    I[a[i]] = I[a[i]] + 1
    if I[a[i]] == 2:
        y2 = y2 + 1
    if I[a[i]] == 4:
        y4 = y4 + 1
    if I[a[i]] == 6:
        y6 = y6 + 1
    if I[a[i]] == 8:
        y8 = y8 + 1
Q = int(sys.stdin.readline().strip())
for q in range(Q):
    (s, x) = sys.stdin.readline().strip().split()
    x = int(x)
    if s == '+':
        I[x] = I[x] + 1
        if I[x] == 2:
            y2 = y2 + 1
        if I[x] == 4:
            y4 = y4 + 1
        if I[x] == 6:
            y6 = y6 + 1
        if I[x] == 8:
            y8 = y8 + 1
    if s == '-':
        I[x] = I[x] - 1
        if I[x] == 1:
            y2 = y2 - 1
        if I[x] == 3:
            y4 = y4 - 1
        if I[x] == 5:
            y6 = y6 - 1
        if I[x] == 7:
            y8 = y8 - 1
    if y4 >= 1 and y2 + y4 + y6 + y8 >= 4:
        print('YES')
    else:
        print('NO')
