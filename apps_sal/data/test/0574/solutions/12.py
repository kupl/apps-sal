ch = input()
d = ch.split(" ")
x1 = int(d[0])
y1 = int(d[1])
x2 = int(d[2])
y2 = int(d[3])

nby = (y2 - y1) // 2 + 1
nbx = (x2 - x1) // 2 + 1
print(nby * nbx + (nby - 1) * (nbx - 1))
