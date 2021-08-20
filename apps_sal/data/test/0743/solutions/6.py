input().split()
xs = list(map(int, input().split()))


def gdc(a, b):
    while b > 0:
        (a, b) = (b, a % b)
    return a


ret = 0
for x in xs:
    ret = gdc(x, ret)
print(ret * len(xs))
