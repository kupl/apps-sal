n = int(input().rstrip())
d = []
for i in range(n):
    w, h = list(map(int, input().rstrip().split()))
    d.append([w, h])
s = '.'
for i in range(len(d)):
    h = d[i][0]
    w = d[i][1]
    f = 1
    for j in range(len(d)):
        if j != i:
            if d[j][0] <= h and d[j][1] <= h:
                w += min(d[j][0], d[j][1])
            elif d[j][0] <= h and d[j][1] > h:
                w += d[j][1]
            elif d[j][0] > h and d[j][1] <= h:
                w += d[j][0]
            else:
                f = 0
    if not f == 0:
        if s == '.' or h * w < s:
            s = h * w
    h = d[i][1]
    w = d[i][0]
    f = 1
    for j in range(len(d)):
        if j != i:
            if d[j][0] <= h and d[j][1] <= h:
                w += min(d[j][0], d[j][1])
            elif d[j][0] <= h and d[j][1] > h:
                w += d[j][1]
            elif d[j][0] > h and d[j][1] <= h:
                w += d[j][0]
            else:
                f = 0
    if not f == 0:
        if s == '.' or h * w < s:
            s = h * w
print(s)
