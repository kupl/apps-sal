(n, m) = list(map(int, input().split()))
c = 0
while n != 0:
    n -= 1
    c += 1
    if c % m == 0:
        n += 1
print(c)
