n, v = map(int, input().split())
cur = 0
total = 0
for i in range(n):
    while cur < n - i - 1:
        cur += 1
        total += (i + 1)
        if cur == v:
            break
    cur -= 1
print(total)
