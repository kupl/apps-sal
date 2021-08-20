def consumed(n, k):
    res = 0
    while n:
        eaten = min(n, k)
        res += eaten
        n -= eaten
        n -= n // 10
    return res


n = int(input())
lo = 1
high = (n + 1) // 2
while lo != high:
    mid = (lo + high) // 2
    if consumed(n, mid) * 2 >= n:
        high = mid
    else:
        lo = mid + 1
print(lo)
