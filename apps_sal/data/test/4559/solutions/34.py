(a, b) = open(0)
c = 1
for i in sorted(b.split()):
    c = [(d := (int(i) * c)), -1][10 ** 18 < d or c < 0]
print(c)
