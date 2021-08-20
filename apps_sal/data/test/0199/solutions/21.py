def ifPoss(arr, v, h):
    tot = 0
    for i in arr:
        tot += i - h
    return tot >= v


def prog():
    (n, v) = map(int, input().split())
    arr = [int(x) for x in input().split()]
    minLev = -1
    (l, h) = (0, min(arr))
    while l <= h:
        m = int((l + h) / 2)
        if ifPoss(arr, v, m):
            minLev = max(minLev, m)
            l = m + 1
        else:
            h = m - 1
    return minLev


print(prog())
