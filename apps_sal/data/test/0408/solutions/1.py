n, m = list(map(int, input().split()))
s = 0

if n > m:
    t = n
    n = m
    m = t

while n > 0 and m > 1:
    n -= 1
    m -= 2
    s += 1
    if n > m:
        t = n
        n = m
        m = t

print(s)

