a, b, x = list(map(int, input().split()))


def c(n):
    d = len(str(n))
    return a * n + b * d <= x


s, t = 0, 10**9 + 1
while s + 1 < t:
    mid = (s + t) // 2
    if c(mid):
        s = mid
    else:
        t = mid

print(s)
