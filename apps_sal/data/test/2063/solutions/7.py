(a, b, c) = list(map(int, input().split(' ')))
l = list(map(int, input().split(' ')))
lo = 0
hi = 2 * 10 ** 9
while lo < hi:
    mid = int((lo + hi + 1) / 2)
    check = mid
    seg = 0
    add = [0] * a
    tot = 0
    for i in range(a):
        if l[i] + seg < check:
            add[i] = check - l[i] - seg
            tot += check - l[i] - seg
            seg += check - l[i] - seg
        if c <= i + 1:
            seg -= add[i - c + 1]
    if tot > b:
        hi = mid - 1
    else:
        lo = mid
print(lo)
