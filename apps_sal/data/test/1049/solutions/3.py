n, d = map(int, input().split())
streak = 0
maximum = 0
for day in range(d):
    c = input()

    if c != "1" * n:
        streak += 1
        maximum = max(maximum, streak)
    else:
        streak = 0

print(maximum)
