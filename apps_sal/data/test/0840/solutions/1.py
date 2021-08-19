(n, k) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
l = 0
r = int(10000000000.0)
while r - l > 1:
    mid = (r + l) // 2
    fail = False
    kk = k
    for i in range(n):
        if b[i] < a[i] * mid:
            if kk > 0:
                kk -= a[i] * mid - b[i]
                if kk < 0:
                    fail = True
            else:
                fail = True
    if fail:
        r = mid
    else:
        l = mid
print(l)
