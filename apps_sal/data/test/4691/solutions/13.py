N = int(input())
C0 = C1 = C2 = C3 = 0
for i in range(N):
    S = str(input())
    if S == 'AC':
        C0 += 1
    if S == 'WA':
        C1 += 1
    if S == 'TLE':
        C2 += 1
    if S == 'RE':
        C3 += 1
C0 = str(C0)
C1 = str(C1)
C2 = str(C2)
C3 = str(C3)
print('AC x ' + C0)
print('WA x ' + C1)
print('TLE x ' + C2)
print('RE x ' + C3)
