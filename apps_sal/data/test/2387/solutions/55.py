import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
A = []
#
PM = [[0, 0] for i in range(n)]
for i in range(n):
    now = 0
    mini = 0
    for j in input():
        if j == "(":
            now += 1
        else:
            now -= 1
            mini = min(mini, now)
    PM[i] = [mini, now]

if sum([PM[i][1] for i in range(n)]) != 0:
    print("No")
    return

MINI = 0
NOW = 0
PMf = [PM[i] for i in range(n) if PM[i][1] >= 0]
PMf.sort()
for i in range(len(PMf)):
    MINI = min(MINI, NOW + PMf[-i - 1][0])
    NOW += PMf[-i - 1][1]
    if MINI < 0:
        print("No")
        return

PMs = [PM[i] for i in range(n) if PM[i][1] < 0]
PMs = sorted(PMs, key=lambda x: x[1] - x[0])
for i in range(len(PMs)):
    MINI = min(MINI, NOW + PMs[-i - 1][0])
    NOW += PMs[-i - 1][1]
    if MINI < 0:
        print("No")
        return

print("Yes")
