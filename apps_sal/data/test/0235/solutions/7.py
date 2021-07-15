def ii():
    return int(input())
def mi():
    return map(int, input().split())
def li():
    return list(mi())
    
def f(n, k):
    c = 0
    e = 0
    while n > 0:
        e += min(k, n)
        n -= k
        n -= n // 10
        c += 1
    return e

n = ii()
lo = 1
hi = th = (n + 1) // 2
while lo < hi:
    mid = (lo + hi) // 2
    cnt = f(n, mid)
    if cnt >= th:
        hi = mid
    else:
        lo = mid + 1
print(lo)
