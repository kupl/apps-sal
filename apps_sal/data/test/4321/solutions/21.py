n, m = [int(i) for i in input().split()]
while m > 0:
    # print(n,m)
    if n % 10 >= m:
        n -= m
        m = 0
    else:
        m = m - n % 10 - 1
        n = n // 10
print(n)
