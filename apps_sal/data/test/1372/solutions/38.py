(h, n), *c = [[*map(int, i.split())]for i in open(0)]
d = [0] * 20002
for i in range(h): d[i] = min(d[i - a] + b for a, b in c)
print(d[h - 1])
