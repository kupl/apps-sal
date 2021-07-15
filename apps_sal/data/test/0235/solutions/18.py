DEBUG = True
n = input().strip().split(" ")
n = int(n[0])

def oneTest(N, k):
    n = N

    nv = 0
    np = 0

    while n > 0:
        if n <= k:
            nv += n
            n = 0
        else:
            n -= k
            nv += k

            x = n // 10
            n -= x
            np += x

    assert nv + np == N
    return nv * 2 >= N


def getResult(n):
    lo = 1
    hi = n
    while lo < hi:
        mid = (lo + hi) // 2
        if not oneTest(n, mid):
            lo = mid + 1
        else:
            hi = mid
    return lo


k = getResult(n)
print(k)

if DEBUG:
    if k > 1:
        assert not oneTest(n, k-1)
    assert oneTest(n, k)
    assert oneTest(n, k+1)

