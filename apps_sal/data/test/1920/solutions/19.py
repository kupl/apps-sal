n = int(input())

females = [0] * 366
males = [0] * 366

for _ in range(n):
    p, start, end = input().split()

    start = int(start) - 1
    end = int(end)

    if p == "F":
        females[start] += 1
        if end < 366:
            females[end] -= 1
    elif p == "M":
        males[start] += 1
        if end < 366:
            males[end] -= 1

cur_m_count = 0
cur_f_count = 0
max_count = 0
for day in range(366):
    cur_m_count += males[day]
    cur_f_count += females[day]
    max_count = max(max_count, 2 * min(cur_f_count, cur_m_count))

print(max_count)
