n = int(input())
half = (n - 1) // 2 + 1


def simulate(k):
    remain = n
    vasya = 0
    while remain > 0:
        vasya += min(k, remain)
        remain -= k
        remain -= remain // 10
    return vasya >= half


hi = n
lo = 0
while hi - lo > 1:
    mid = (hi + lo) // 2
    if simulate(mid):
        hi = mid
    else:
        lo = mid
print(hi)
