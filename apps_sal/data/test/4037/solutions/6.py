from sys import stdin, stdout
import math
import copy

N, r = [int(x) for x in stdin.readline().split()]

visited = [0] * N

a = [0] * N
b = [0] * N

pos = 0

dp = {}

for i in range(N):
    arr = [int(x) for x in stdin.readline().split()]
    a[i] = arr[0]
    b[i] = arr[1]

    if b[i] >= 0:
        pos += 1

valid = 0
for i in range(pos):
    idx = -1
    start = 0
    gain = -50000
    for j in range(N):
        if visited[j] == 1 or b[j] < 0:
            continue

        if b[j] > gain and r >= a[j]:
            gain = b[j]
            idx = j
            start = a[j]
        elif b[j] == gain and r >= a[j]:
            if a[j] > start:
                idx = j
                start = a[j]

    if idx == -1:
        break
    else:
        visited[idx] = 1
        r += b[idx]
        valid = i + 1

dp[r] = valid
tmp = []
for i in range(N):
    if visited[i] == 1 or b[i] >= 0:
        continue
    tmp.append((a[i], b[i], i))

tmp.sort(key=lambda e: (e[0] + e[1], e[0]), reverse=True)

for i in range(len(tmp)):
    dp_tmp = copy.deepcopy(dp)

    for threshold in dp:
        if threshold >= tmp[i][0]:
            new_r = threshold + tmp[i][1]
            if new_r in dp_tmp:
                dp_tmp[new_r] = max(dp[new_r], dp[threshold] + 1)
            else:
                dp_tmp[new_r] = dp[threshold] + 1

    dp = dp_tmp

res = 0
for key in dp:
    if key >= 0:
        res = max(res, dp[key])

print(res)
