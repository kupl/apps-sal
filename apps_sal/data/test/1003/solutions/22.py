n, m = map(int, input().split())

d = 1
while n > 0:
    if d % m == 0:
        n += 1
    n -= 1
    d += 1


print(d - 1)
