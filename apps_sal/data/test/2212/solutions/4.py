n = int(input())
c = n // 2
m = []
o = 1
e = 2
for i in range(n):
    row = []
    for j in range(n):
        if abs(i - c) + abs(j - c) <= c:
            row.append(str(o))
            o += 2
        else:
            row.append(str(e))
            e += 2
    m.append(row)
for row in m:
    print(" ".join(row))

