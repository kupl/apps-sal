N = int(input())
S = [input() for i in range(N)]
A = 0
W = 0
T = 0
R = 0
for i in range(len(S)):
    if S[i] == 'AC':
        A += 1
    elif S[i] == 'WA':
        W += 1
    elif S[i] == 'TLE':
        T += 1
    else:
        R += 1
print('AC x ' + str(A))
print('WA x ' + str(W))
print('TLE x ' + str(T))
print('RE x ' + str(R))
