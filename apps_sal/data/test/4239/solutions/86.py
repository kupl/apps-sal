from collections import deque
N = int(input())
units = set()
i = 0
while 6 ** i <= N:
    units.add(6 ** i)
    i += 1
i = 0
while 9 ** i <= N:
    units.add(9 ** i)
    i += 1
units = sorted(units)
mins = list(range(N + 1))
for i in range(1, len(units)):
    unit = units[i]
    for j in range(N):
        if j + unit < len(mins) and mins[j] + 1 < mins[j + unit]:
            mins[j + unit] = mins[j] + 1
print(mins[N])
