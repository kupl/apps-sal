n = int(input())
L = [0] * 101
for i in range(n):
    L[int(input())] += 1
S = set()
for i in range(len(L)):
    if L[i]:
        S.add(i)
if len(S) == 2:
    M = list(S)
    if L[M[0]] == L[M[1]]:
        print('YES')
        print(M[0], M[1])
    else:
        print('NO')    
else:
    print('NO')

