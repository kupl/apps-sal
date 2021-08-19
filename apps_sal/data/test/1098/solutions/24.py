n = int(input())
alarms = []
for i in range(n):
    (h, m) = list(map(int, input().split(':')))
    t = h * 60 + m
    alarms.append(t)
alarms.sort()
alarms.append(alarms[0] + 24 * 60)
mx = -1
for i in range(1, len(alarms)):
    if mx < alarms[i] - alarms[i - 1]:
        mx = alarms[i] - alarms[i - 1]
mx -= 1
print('{:02d}:{:02d}'.format(mx // 60, mx % 60))
