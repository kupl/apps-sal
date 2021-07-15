n, m = map(int, input().split())
res = 0
if n >= m:
    res = n - m
else:
    while m > n:
        if m % 2 == 1:
            m += 1
        else:
            m //= 2
        res += 1
    res += (n - m)
print(res)
