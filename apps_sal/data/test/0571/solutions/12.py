from itertools import accumulate
N = int(input())
S = input()
if S[0] == ')' or S[-1] == '(' or N % 2 == 1:
    print(':(')
    return
L = [0]*N
posi = 0
nega = 0
for i, s in enumerate(S):
    if s == '(':
        posi += 1
        L[i] = 1
        continue
    elif s == ')':
        nega += 1
        L[i] = -1
        continue
rem = N - posi - nega
sp = nega - posi
pi = (rem + sp)//2
ni = (rem - sp)//2
if pi < 0 or ni < 0:
    print(':(')
    return
LP = L.copy()
for i, a in enumerate(L):
    if not a:
        if pi > 0:
            pi -= 1
            LP[i] = 1
        else:
            LP[i] = -1
if all([i > 0 for i in list(accumulate(LP))[:-1]]):
    print(''.join([('', '(', ')')[l] for l in LP]))
    return
print(':(')
