import sys
a, n, m = list(map(int, input().split(' ')))

seg = []
for i in range(n):
    rained = tuple(map(int, input().split(' ')))
    for k in range(rained[0], rained[1]):
        seg.append(k+1)

umbrella = []
for j in range(m):
    u = tuple(map(int, input().split(' ')))
    umbrella.append(u)

memo = [0] * (a+1)

umbrella = sorted(umbrella, key=lambda x: x[0])
if umbrella[0][0] > seg[0] - 1:
    print(-1)
    return

for index in range(1, len(memo)):

    if index not in seg:
        memo[index] = memo[index-1]
        continue

    for each in umbrella:
        if index >= each[0]:
            cur = (index - each[0]) * each[1] + memo[each[0]]
            if memo[index] > 0:
                if cur < memo[index]:
                    memo[index] = cur
            else:
                memo[index] = cur






print(memo[-1])











