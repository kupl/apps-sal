def square(n):
    if n < 0:
        return False
    lo = 0
    hi = n
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid * mid > n:
            hi = mid
        if mid * mid < n:
            lo = mid
        if mid * mid == n:
            return True
    if lo * lo == n or hi * hi == n:
        return True
    return False


n = int(input())
line = input().split()

best = -10**7
for i in range(n):
    a = int(line[i])
    if not square(a):
        best = max(best, a)
print(best)
