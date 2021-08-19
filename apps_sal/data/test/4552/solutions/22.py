import numpy as np
N = int(input())
schedules = [list(map(int, input().split())) for _ in range(N)]
prices = [list(map(int, input().split())) for _ in range(N)]
# print(schedules)
# print(prices)
ans = -1 * float('inf')
for i in range(1, 1 << 10):
    my_schedule = list(map(int, bin(i)[2:].zfill(10)))
    score = 0
    for j, schedule in enumerate(schedules):
        count = 0
        for k in range(10):
            if my_schedule[k] == schedule[k] and schedule[k] == 1:
                count += 1
        score += prices[j][count]
    ans = max(ans, score)
print(ans)
