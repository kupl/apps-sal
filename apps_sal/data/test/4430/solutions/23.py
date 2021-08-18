
n, k, m = list(map(int, input().split()))
l = [int(i) for i in input().split()]


def ispzbl(l, n, m, k, mid):
    z = l[mid:]
    if not z:
        return True
    s = 0
    box = 1
    for i in z:
        s += i
        if s > m:
            box += 1
            s = i
    return box <= k


low = 0
high = n - 1
while low <= high:
    mid = (low + high) // 2
    if ispzbl(l, n, m, k, mid):
        ans = mid
        high = mid - 1
    else:
        low = mid + 1
print(n - ans)
