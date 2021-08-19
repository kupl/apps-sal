(n, m) = map(int, input().split())
(day, c) = (0, 1)
while n != 0:
    day += 1
    if day == c * m:
        n += 1
        c += 1
    n -= 1
print(day)
