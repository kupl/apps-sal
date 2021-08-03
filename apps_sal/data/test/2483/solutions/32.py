from itertools import accumulate
n, C = list(map(int, input().split()))

U = 10**5
channels = [[0] * (U + 1) for _ in range(C)]
for _ in range(n):
    s, t, c = [int(x) - 1 for x in input().split()]
    channels[c][s] += 1
    channels[c][t] -= 1


for i in range(C):
    for j in range(U):
        channels[i][j + 1] += channels[i][j]

schedules = [0] * (U + 1)
for i in range(C):
    L = None
    for j in range(U + 1):
        if channels[i][j] and L is None:
            L = j - 1
            continue

        if not channels[i][j] and L is not None:
            schedules[max(L, 0)] += 1
            schedules[j] -= 1
            L = None

print((max(accumulate(schedules))))
