N = int(input())

C0 = 0
C1 = 0
C2 = 0
C3 = 0

for i in range(N):
    Si = input()
    if Si == 'AC':
        C0 += 1
    elif Si == 'WA':
        C1 += 1
    elif Si == 'TLE':
        C2 += 1
    elif Si == 'RE':
        C3 += 1
print('AC x ' + str(C0))
print('WA x ' + str(C1))
print('TLE x ' + str(C2))
print('RE x ' + str(C3))
