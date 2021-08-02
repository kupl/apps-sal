def R(): return map(int, input().split())


n, m = R()
color = dict()
for i in range(m):
    d = list(R())
    temp = 0
    for j in d:
        if j in color:
            temp = temp | (1 << color[j])
    for j in range(3):
        if d[j] not in color:
            for k in range(3):
                if not ((1 << (k + 1)) & temp):
                    color[d[j]] = k + 1
                    temp = temp | (1 << k + 1)
                    break
for i in range(n):
    print(color[i + 1], end=' ')
print()
