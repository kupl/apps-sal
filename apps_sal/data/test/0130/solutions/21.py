def polycarp(n, m, l):
    left = min(l).find("B")
    if left == -1:
        return 1
    right = m - min([x[::-1] for x in l]).find("B") - 1
    top = bottom = -1
    for i in range(n):
        if l[i].find("B") != -1:
            top = i
            break
    for i in range(n - 1, -1, -1):
        if l[i].find("B") != -1:
            bottom = i
            break
    w = right - left + 1
    h = bottom - top + 1
    if w > n or h > m:
        return -1
    r = 0
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if l[i][j] == "W":
                r += 1
    if w > h:
        r += (w - h) * w
    else:
        r += (h - w) * h
    return r


n, m = list(map(int, input().strip().split()))
l = list()
for i in range(n):
    l.append(input().strip())
print(polycarp(n, m, l))
