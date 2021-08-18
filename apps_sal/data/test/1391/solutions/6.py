def readn():
    return list(map(int, input().split()))


n, m, a = readn()
b, p = sorted(map(int, input().split()))[-min(n, m):], sorted(map(int, input().split()))
r = min(n, m)
mm = r
l = 0
while l <= r:
    mid = l + (r - l) // 2
    pri = sum([max(0, p[i] - b[mm - mid + i]) for i in range(mid)])
    if pri <= a:
        l = mid + 1
    else:
        r = mid - 1
print(r, max(0, sum(p[:r]) - a))
