n = int(input())
tm = tuple(map(int, input().split(':')))
cost = [[0 for i in range(100)] for j in range(100)]
for i in range(100):
    for j in range(100):
        (x, y) = (i, j)
        for k in range(2):
            cost[i][j] += x % 10 != y % 10
            x //= 10
            y //= 10
hr_range = list(range(1, 13))
if n == 24:
    hr_range = list(range(0, 24))
best_time = None
best_val = 123
for h in hr_range:
    for m in range(60):
        cur = cost[h][tm[0]] + cost[m][tm[1]]
        if cur < best_val:
            best_val = cur
            best_time = '{:02d}:{:02d}'.format(h, m)
print(best_time)
