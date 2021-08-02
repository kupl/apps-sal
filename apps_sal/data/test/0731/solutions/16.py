def f(x):
    digs = len(str(x))

    ndig = digs * (x - 10**(digs - 1) + 1)
    for i in range(1, digs):
        ndig += i * 9 * 10**(i - 1)
    return ndig


a, b, c = list(map(int, input().split(' ')))
num = a // c

need = num + f(b - 1)

lo = 0
hi = 10**18

while lo < hi:
    mid = (lo + hi + 1) // 2
    if f(mid) > need:
        hi = mid - 1
    else:
        lo = mid
print(lo - b + 1)
