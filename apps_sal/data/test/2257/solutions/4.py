(n, x1, y1, x2, y2) = list(map(int, input().split()))
x = []
y = []
for i in range(n):
    (xx, yy) = list(map(int, input().split()))
    x.append(xx)
    y.append(yy)
ans = int(1000000000000000000)
for i in range(n):
    flag = []
    for j in range(n):
        flag.append(0)
    tt = (x[i] - x1) * (x[i] - x1) + (y[i] - y1) * (y[i] - y1)
    for j in range(n):
        ss = (x[j] - x1) * (x[j] - x1) + (y[j] - y1) * (y[j] - y1)
        if ss <= tt:
            flag[j] = 1
    hh = int(0)
    for j in range(n):
        if flag[j] == 1:
            continue
        ss = (x[j] - x2) * (x[j] - x2) + (y[j] - y2) * (y[j] - y2)
        hh = max(hh, ss)
    ans = min(ans, hh + tt)
jj = 0
for i in range(n):
    tt = (x[i] - x1) * (x[i] - x1) + (y[i] - y1) * (y[i] - y1)
    jj = max(jj, tt)
ans = min(ans, jj)
jj = 0
for j in range(n):
    ss = (x[j] - x2) * (x[j] - x2) + (y[j] - y2) * (y[j] - y2)
    jj = max(jj, ss)
ans = min(ans, jj)
print(ans)
