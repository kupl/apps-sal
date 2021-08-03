n, m = input().split()
n = int(n)
m = int(m)
flag = 0
res = 0
if m > n:
    print(-1)
else:
    while n >= 2 * m:
        res += m
        n -= 2 * m
    if n % (2 * m) != 0:
        res += m
    print(res)
