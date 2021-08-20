(n, m) = map(int, input().split())
day = 1
while n > 0:
    n -= 1
    if day % m == 0:
        n += 1
    day += 1
print(day - 1)
