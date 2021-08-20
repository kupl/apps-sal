(a, b, c) = list(map(int, input().split()))
cost = [0, 1, 2, 0, 2, 1, 0]
dcost = [3, 2, 2]
weeks = min(a // 3, b // 2, c // 2)
left = [a - 3 * weeks, b - 2 * weeks, c - 2 * weeks]
cost = cost + cost
maxdays = 0
for i in range(7):
    l = left[:]
    days = 0
    for j in range(i, i + 7):
        if l[cost[j]] == 0:
            break
        days += 1
        l[cost[j]] -= 1
    maxdays = max(maxdays, days)
print(weeks * 7 + maxdays)
