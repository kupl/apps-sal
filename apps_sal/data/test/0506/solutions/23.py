n, m = [int(x) for x in input().split()]
c, mn, mx = 0, 0, 0
while n != m and n > 0 and m > 0:
    p = max(n, m) // min(n , m)
    c += p
    if n > m:
        n -= p * m
    else:
        m -= p * n
print(c)


