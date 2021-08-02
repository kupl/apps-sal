g, d, f = (int(s) for s in input().split())
gs = sorted([int(s) for s in input().split()])
ds = sorted([int(s) for s in input().split()])
fs = sorted([int(s) for s in input().split()])

gn = [0] * 100001
dn = [0] * 100001
fn = [0] * 100001

for a in gs:
    gn[a] += 1

for a in ds:
    dn[a] += 1

for a in fs:
    fn[a] += 1

gx = 0
dx = 0
fx = 0

for i in range(100001):
    gx += gn[i]
    dx += dn[i]
    fx += fn[i]

    gn[i] = gx
    dn[i] = dx
    fn[i] = fx


def team_count(a, b):
    if a > 100000:
        a = 100000
    if b > 100000:
        b = 100000
    gc = gn[b] - gn[a]
    dc = dn[b] - dn[a]
    fc = fn[b] - fn[a]

    val = gc * dc * (dc - 1) * fc * (fc - 1) * (fc - 2) // 12
    if val < 0:
        print(val)
    return val


res = team_count(0, 2)
for i in range(1, 50001):
    res += team_count(i, 2 * i + 2) - team_count(i, 2 * i)

print(res)
