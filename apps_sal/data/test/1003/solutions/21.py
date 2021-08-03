n, m = list(map(int, input().split()))
now = n
day = 1
while now > 0:
    now -= 1
    if day % m == 0:
        now += 1
    day += 1
print(day - 1)
