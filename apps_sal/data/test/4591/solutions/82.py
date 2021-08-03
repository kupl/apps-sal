a, b, c, x, y = list(map(int, input().split()))
mmin = -1


def maxint(x, y: int) -> int:
    if x > y:
        return x
    else:
        return y


max = maxint(x, y)
for i in range(0, max + 1):
    tmp = 2 * c * i + a * (maxint(0, x - i)) + b * (maxint(0, y - i))
    if mmin == -1:
        mmin = tmp
        continue
    if tmp < mmin:
        mmin = tmp
print(mmin)
