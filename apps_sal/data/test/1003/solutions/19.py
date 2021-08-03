n, m = list(map(int, input().split()))
day = 0
while True:
    if n == 0:
        print(day)
        break
    n -= 1
    if day % m == m - 1:
        n += 1
    day += 1
