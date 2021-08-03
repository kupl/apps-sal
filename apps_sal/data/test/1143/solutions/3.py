from collections import Counter
dm = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def dec(d):
    d[2] -= 1
    if d[2] == 0:
        d[1] -= 1
        if d[1] == 0:
            d[0] -= 1
            d[1] = 12
        d[2] = dm[d[1]]


f = open('input.txt', 'r')
c = Counter()
for i in range(int(f.readline())):
    d = [2013] + list(map(int, f.readline().split()))
    for j in range(d[4]):
        dec(d)
        c[10000 * d[0] + 100 * d[1] + d[2]] += d[3]
print(c.most_common()[0][1], file=open('output.txt', 'w'))
