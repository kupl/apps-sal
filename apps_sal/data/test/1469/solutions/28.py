L = int(input())

r = 0
while 2 ** r <= L:
    r += 1

E = []
for i in range(1, r):
    E.append((i, i + 1, 0))
    E.append((i, i + 1, 2 ** (i - 1)))

# 2**(r-1) ～ L-1 のPATHがない。

n = 2 ** (r - 1)

###
while True:
    d = L - 1 - n + 1
    if d <= 0:
        break
    zi = 0
    while 2 ** (zi) <= d:
        zi += 1

    E.append((zi, r, n))
    n = n + 2 ** (zi - 1)

print(("{} {}".format(r, len(E))))

for e in E:
    print(("{} {} {}".format(e[0], e[1], e[2])))

