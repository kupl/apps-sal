from collections import defaultdict
from itertools import accumulate
(N, K) = map(int, input().split())
timetables = defaultdict(list)
for i in range(N):
    (s, t, c) = map(int, input().split())
    timetables[c].append([s, t])
for (name, times) in timetables.items():
    times.sort()
    new = []
    for (i, time) in enumerate(times):
        (s, t) = time
        if i == 0:
            new.append([s, t])
            continue
        if s == new[-1][1]:
            new[-1][1] = t
        else:
            new.append([s, t])
    timetables[name] = new
time_count = [0] * 100010
for (name, times) in timetables.items():
    for (s, t) in times:
        time_count[s] += 1
        time_count[t + 1] -= 1
acc = accumulate(time_count)
print(max(acc))
