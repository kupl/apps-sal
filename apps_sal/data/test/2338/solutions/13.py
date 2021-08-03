import sys
input = sys.stdin.readline
print = sys.stdout.write
def I(): return list(map(int, input().split()))


n, = I()
l = []
r = []
k = 0
for i in range(n):
    x, y = I()
    if x < 0:
        l.append([x, y])
    else:
        r.append([x, y])
    k = k + 4 if x != 0 and y != 0 else k + 2

k += 2 * n
an = []
l.sort(key=lambda x: abs(x[0]) + abs(x[1]))
r.sort(key=lambda x: abs(x[0]) + abs(x[1]))
for i in range(len(r)):
    x, y = r[i]
    if x != 0:
        an.append("1 %d R" % x)
    if y != 0:
        an.append("1 %d %s" % (abs(y), ("U" if y > 0 else "D")))
    an.append('2')
    if x != 0:
        an.append("1 %d L" % x)
    if y != 0:
        an.append("1 %d %c" % (abs(y), ('D' if y > 0 else 'U')))
    an.append('3')

for i in range(len(l)):
    x, y = l[i]
    x = -x
    if x != 0:
        an.append("1 %d L" % x)
    if y != 0:
        an.append("1 %d %c" % (abs(y), ('U' if y > 0 else 'D')))
    an.append('2')
    if x != 0:
        an.append("1 %d R" % x)
    if y != 0:
        an.append("1 %d %c" % (abs(y), ('D' if y > 0 else 'U')))
    an.append('3')
print(str(k) + '\n')
print("\n".join(an))
