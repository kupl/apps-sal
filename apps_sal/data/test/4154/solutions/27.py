N, M = map(int, input().split())
L = []
R = []

for i in range(M):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

Rm = min(R)
LM = max(L)

if Rm - LM >= 0:
    print(Rm - LM + 1)

else:
    print(0)
