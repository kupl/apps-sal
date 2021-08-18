import copy
import sys
readline = sys.stdin.readline

N, C = map(int, readline().split())
sushi = [list(map(int, readline().split())) for i in range(N)]
revsushi = copy.deepcopy(sushi)[::-1]
for i in range(len(sushi) - 1, 0, -1):
    sushi[i][0] = sushi[i][0] - sushi[i - 1][0]

for i in range(len(revsushi)):
    revsushi[i][0] = C - revsushi[i][0]
for i in range(len(revsushi) - 1, 0, -1):
    revsushi[i][0] = revsushi[i][0] - revsushi[i - 1][0]

left = [[0] * 2 for i in range(N + 1)]
right = [[0] * 2 for i in range(N + 1)]

left[0] = [0, 0]
right[0] = [0, 0]

for i in range(len(sushi)):
    x, v = sushi[i]
    left[i + 1][0] = left[i][0] + v - x
    if left[i + 1][0] > left[i][1]:
        left[i + 1][1] = left[i + 1][0]
    else:
        left[i + 1][1] = left[i][1]

best = left[-1][1]
cal = 0
for i in range(len(revsushi)):
    count = i + 1
    lp = left[N - count][1]
    x, v = revsushi[i]
    cal += (v - x * 2)
    if lp + cal > best:
        best = lp + cal

for i in range(len(revsushi)):
    x, v = revsushi[i]
    right[i + 1][0] = right[i][0] + v - x
    if right[i + 1][0] > right[i][1]:
        right[i + 1][1] = right[i + 1][0]
    else:
        right[i + 1][1] = right[i][1]

best = max(best, right[-1][1])
cal = 0
for i in range(len(sushi)):
    count = i + 1
    rp = right[N - count][1]
    x, v = sushi[i]
    cal += (v - x * 2)
    if rp + cal > best:
        best = rp + cal

print(best)
