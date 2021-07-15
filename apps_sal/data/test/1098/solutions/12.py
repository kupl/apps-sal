n = int(input())
alarms = []
for i in range (n):
    line = [int(x) for x in input().strip().split(':')]
    alarms.append(line[0] * 60 + line[1])
alarms = sorted(alarms)
tmp = [1440 + x for x in alarms]
alarms += tmp
ans = 0
for i in range(1, len(alarms)):
    if (i > 0):
        ans = max(ans, alarms[i] - alarms[i - 1] - 1)
print("%02d:%02d" % (ans // 60, ans % 60))
