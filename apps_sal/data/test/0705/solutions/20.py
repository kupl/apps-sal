import sys


def gis():
    l = sys.stdin.readline().strip()
    parts = l.split()
    return list(map(int, parts))


n, = gis()
xs = gis()
ys = gis()

nums = set(xs + ys)
cnt = 0
for x in xs:
    for y in ys:
        if (x ^ y) in nums:
            cnt += 1

if cnt % 2 == 0:
    print('Karen')
else:
    print('Koyomi')
