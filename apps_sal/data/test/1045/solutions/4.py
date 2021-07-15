n, cur, i = int(input()), 0, 0
while cur <= n:
    i += 1
    cur += i * (i + 1) // 2
print(i - 1)
