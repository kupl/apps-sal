3.5

N, M = [*list(map(int, input().split()))]
_L = [list() for i in range(0, M)]

for i in range(0, N):
    s, r = [*list(map(int, input().split()))]
    _L[s-1].append(r)

L = []
L_sum = []

for x in _L:
    if len(x) != 0:
        x.sort(reverse=True)
        L.append(x)

L.sort(reverse=True, key=lambda x: len(x))
for x in L:
    _s = [0]*len(x)
    _s[0] = x[0]

    for i in range(1, len(x)):
        _s[i] = _s[i-1] + x[i]

    L_sum.append(_s)
        
ret = 0
for i in range(1, N+1):
    cpt = 0
    for j in range(0, len(L)):
        if len(L[j]) < i:
            break
        
        if L_sum[j][i-1] > 0:
            cpt += L_sum[j][i-1]

    ret = max(ret, cpt)

print(max(0, ret))

