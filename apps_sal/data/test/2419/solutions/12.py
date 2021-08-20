t = int(input())


def bin_search(d, lo, hi):
    if lo + 1 == hi:
        return hi
    mid = (lo + hi) // 2
    if mid * (mid + 1) // 2 >= d:
        hi = mid
    else:
        lo = mid
    return bin_search(d, lo, hi)


for _ in range(t):
    (a, b) = list(map(int, input().split()))
    d = abs(a - b)
    if d == 0:
        print(0)
        continue
    count = bin_search(d, 0, 10 ** 6)
    while count * (count + 1) // 2 % 2 != d % 2:
        count += 1
    print(count)
