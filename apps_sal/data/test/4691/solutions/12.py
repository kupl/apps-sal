N = int(input())
AC = 0
WA = 0
TLE = 0
RE = 0
for i in range(N):
    s = input()
    if(s == 'AC'):
        AC += 1
    elif(s == 'WA'):
        WA += 1
    elif(s == 'TLE'):
        TLE += 1
    elif(s == 'RE'):
        RE += 1

print('AC x ' + str(AC))
print('WA x ' + str(WA))
print('TLE x ' + str(TLE))
print('RE x ' + str(RE))
