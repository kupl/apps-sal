n, m = [int(x) for x in input().split()]
i = 0
while n > 0:
    n -= 1
    i += 1
    if i % m == 0:
        n += 1
print(i)
