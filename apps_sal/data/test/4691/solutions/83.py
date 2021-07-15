N = int(input())
C = 0
D = 0
E = 0
F = 0
S = ''

for i in range(N):
    S = input()
    if S == 'AC':
        C += 1
    elif S == 'WA':
        D += 1
    elif S == 'TLE':
        E += 1
    elif S == 'RE':
        F += 1
print('AC x '+ str(C), 'WA x ' + str(D),  'TLE x ' + str(E),  'RE x ' + str(F), sep='\n')

