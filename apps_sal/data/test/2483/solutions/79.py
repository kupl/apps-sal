import itertools
(N, C) = list(map(int, input().split()))
ch = [[] for _ in range(C + 1)]
time = [0] * (10 ** 5 + 1)
for _ in range(N):
    (s, t, c) = list(map(int, input().split()))
    ch[c].append(s)
    ch[c].append(t)
for i in range(1, C + 1):
    ch[i].sort()
for i in range(1, C + 1):
    for chi in range(len(ch[i])):
        if chi % 2 == 0:
            if chi == 0:
                time[ch[i][chi] - 1] += 1
            elif chi > 1 and ch[i][chi - 1] != ch[i][chi]:
                time[ch[i][chi] - 1] += 1
        elif chi % 2 == 1:
            if chi == len(ch[i]) - 1:
                time[ch[i][chi]] -= 1
            elif ch[i][chi + 1] != ch[i][chi]:
                time[ch[i][chi]] -= 1
integ_time = itertools.accumulate(time)
print(max(integ_time))
