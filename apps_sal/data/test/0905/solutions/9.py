n, s = [int(i) for i in input(). split()]
x = [0] * n
y = [0] * n
smin = 100
for i in range(n):
    x[i], y[i] = [int(x) for x in input(). split()]
    if (x[i] < s) and (y[i] < smin) and (y[i] != 0):
        smin = y[i]
if smin == 100:
    smin = -1
    for i in range(n):
        if (x[i] <= s) and (y[i] == 0):
            smin = 0
    print(smin)
else:
    print(100 - smin)
