A = []
P = ['o']*9
for i in range(3):
    a = [int(i) for i in input().split()]
    for j in range(3):
        A.append(a[j])

N = int(input())
for i in range(N):
    b = int(input())
    for j in range(9):
        if A[j] == b:
            P[j] = 'x'

t = 0
for i in range(3):
    if (P[i] == P[i+3] == P[i+6] == 'x') or (P[3*i] == P[3*i+1] == P[3*i+2] == 'x'):
        t += 1
        break
if (P[0] == P[4] == P[8] == 'x') or (P[2] == P[4] == P[6] == 'x'):
    t += 1

if t == 0:
    print('No')
else:
    print('Yes')
