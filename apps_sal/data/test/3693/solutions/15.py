def rf():
    cs = list(map(int, input().split(' ')))
    cs = list(zip(cs[0::2], cs[1::2]))
    return cs

# Cross product of vectors (p1-p) and (p2-p)
def cross(p, p1, p2):
    return (p2[1] - p[1]) * (p1[0] - p[0]) - (p2[0] - p[0]) * (p1[1] - p[1])

# p = (x, y)
# f = [(x1, y1), (x2, y2), ...]
def inside(p, f):
    os = 0
    total = 0
    for i in range(len(f)):
        p1 = f[i]
        p2 = f[(i+1)%len(f)]
        delta = cross(p, p1, p2)

        os += delta
        total += abs(delta)

    os = abs(os)
    return os == total

fs = [rf(), rf()]

res = False
for f1, f2 in [fs, fs[::-1]]:
    for p in f1:
        if inside(p, f2):
            res = True
    if inside( ( (f1[0][0] + f1[2][0]) // 2, (f1[0][1] + f1[2][1]) // 2 ), f2 ):
        res = True

print(['NO', 'YES'][res])

