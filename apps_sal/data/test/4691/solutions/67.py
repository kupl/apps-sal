N = int(input())
S = [input() for S in range(N)]
C = [0, 0, 0, 0]
for i in range(N):
    if S[i] == 'AC':
        C[0] += 1
    elif S[i] == 'WA':
        C[1] += 1
    elif S[i] == 'TLE':
        C[2] += 1
    elif S[i] == 'RE':
        C[3] += 1
print('AC x ', C[0])
print('WA x ', C[1])
print('TLE x ', C[2])
print('RE x ', C[3])
