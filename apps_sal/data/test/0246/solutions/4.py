def f(n):
    rtn = n
    while 0 < n:
        rtn -= n % 10
        n //= 10
    return rtn

n, s = list(map(int, input().split()))
l = 0
r = 10**18 + 1
cnt = 0
while 1 < r - l:
    m = (l + r) // 2
    if s <= f(m):
        r = m
    else:
        l = m

print(max(n - r + 1, 0))

