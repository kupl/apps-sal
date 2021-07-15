n, d = map(int, input().split())

days = 0
max_days = 0
for i in range(d):
    if '0' in input():
        days += 1
        max_days = max(days, max_days)
    else:
        days = 0
print(max_days)
