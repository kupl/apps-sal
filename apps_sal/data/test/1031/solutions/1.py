import operator


n = int(input())
a = tuple(map(int, str.split(input())))

p = [(0, 0)]
for i, x in enumerate(a):

    p.append((p[-1][0] + x, p[-1][1] + (-1) ** i * x))

ymax = max(p, key=operator.itemgetter(1))[1]
ymin = min(p, key=operator.itemgetter(1))[1]

columns = []
for i in range(n):

    x1, y1 = p[i]
    x2, y2 = p[i + 1]
    while x1 != x2:

        if y1 < y2:

            columns.append(" " * (ymax - y1 - 1) + "/" + " " * (y1 - ymin))
            y1 += 1

        else:

            columns.append(" " * (ymax - y1) + "\\" + " " * (y1 - ymin - 1))
            y1 -= 1

        x1 += 1

print(str.join("\n", [str.join("", t) for t in zip(*columns)]))

