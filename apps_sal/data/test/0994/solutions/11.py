n, m = map(int, input().split())
d, h = [], []
for i in range(m):
    di, hi = map(int, input().split())
    d.append(di)
    h.append(hi)
maximum = h[0]
if d[0] != 1:
    d.insert(0, 1)
    h.insert(0, -1)
    m += 1
flag = 0
for i in range(1, m):
    diff = d[i] - d[i - 1]
    if h[i - 1] == -1:
        if diff + h[i] > maximum:
            maximum = diff + h[i]
    else:
        if abs(h[i] - h[i - 1]) > diff:
            flag = 1
            break
        elif abs(h[i] - h[i - 1]) < diff:
            p = diff - (abs(h[i - 1] - h[i]))
            if max(h[i], h[i - 1]) + p // 2 > maximum:
                maximum = p // 2 + max(h[i], h[i - 1])
        else:
            if max(h[i], h[i - 1]) > maximum:
                maximum = max(h[i], h[i - 1])
if d[m - 1] < n:
    if maximum < h[m - 1] + n - d[m - 1]:
        maximum = h[m - 1] + n - d[m - 1]
if flag == 1:
    print("IMPOSSIBLE")
else:
    print(maximum)
