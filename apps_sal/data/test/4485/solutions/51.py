N, M = list(map(int, input().split()))
L = [list(map(int, input().split())) for i in range(M)]
s = []
g = []
for i in range(M):
    if 1 == L[i][0]:
        s.append(L[i][1])
    if 1 == L[i][1]:
        s.append(L[i][0])

for i in range(M):
    if N == L[i][0]:
        g.append(L[i][1])
    if N == L[i][1]:
        g.append(L[i][0])

if set(g) & set(s):
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
