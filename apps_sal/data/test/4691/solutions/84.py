N = int(input())
S = []
AC = 0
TLE = 0
WA = 0
RE = 0

for i in range(0, N):
    S.append(input())
    if S[i] == 'AC':
        AC += 1
    elif S[i] == 'TLE':
        TLE += 1
    elif S[i] == 'WA':
        WA += 1
    elif S[i] == 'RE':
        RE += 1

print('AC x %d' % AC)
print('WA x %d' % WA)
print('TLE x %d' % TLE)
print('RE x %d' % RE)
