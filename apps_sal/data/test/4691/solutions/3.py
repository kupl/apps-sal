n = int(input())
(AC, WA, TLE, RE) = (0, 0, 0, 0)
for x in range(n):
    s = input()
    if s == 'AC':
        AC = AC + 1
    elif s == 'WA':
        WA = WA + 1
    elif s == 'TLE':
        TLE = TLE + 1
    elif s == 'RE':
        RE = RE + 1
print('AC x ' + str(AC))
print('WA x ' + str(WA))
print('TLE x ' + str(TLE))
print('RE x ' + str(RE))
