n,m,k = list(map(int,input().split()))
l, r = 1, 10 ** 9 + 1

def ok(p):
    rs = 0
    if k >= p:
        rs += p * (p + 1) // 2
        rs += (k - p)
    else:
        rs += p * (p + 1) // 2
        f = p - k
        rs -= f * (f + 1) // 2
    if (p - 1) <= n - k:
        rs += p * (p - 1) // 2
        rs += n - k - p + 1
    else:
        rs += p * (p - 1) // 2
        f = (p - 1) - (n - k)
        rs -= f * (f + 1) // 2
    return rs <= m

while r - l > 1:
    mid = (l + r) // 2
    if ok(mid):
        l = mid
    else:
        r = mid
print(l)
