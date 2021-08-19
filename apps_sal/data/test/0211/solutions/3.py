def chk(x):
    d = (m - x) // (k - 1) * k
    if (m - x) % (k - 1):
        d += 1 + (m - x) % (k - 1)
    if d <= n - x:
        return True
    else:
        return False


def calc(e):
    if e == 1:
        return 2
    if e & 1:
        d = 2
    else:
        d = 1
    f = calc(e >> 1)
    d = d * f % D * f % D
    return d


(n, m, k) = list(map(int, input().split()))
D = 1000000009
l = 0
h = n
while l < h:
    mid = l + h >> 1
    if chk(mid):
        h = mid
    else:
        l = mid + 1
h = calc(l // k + 1) - 2
if h < 0:
    h += D
print((k * h % D + m - l // k * k) % D)
