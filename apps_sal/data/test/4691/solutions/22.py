N = int(input())
result = []
for i in range(N):
    r = input()
    result.append(r)
AC = 0
WA = 0
TLE = 0
RE = 0
for i in range(N):
    if result[i] == 'AC':
        AC += 1
    if result[i] == 'WA':
        WA += 1
    if result[i] == 'TLE':
        TLE += 1
    if result[i] == 'RE':
        RE += 1
print('AC x', AC)
print('WA x', WA)
print('TLE x', TLE)
print('RE x', RE)
