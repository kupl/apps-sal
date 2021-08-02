import math
L = []
S = []
for i in range(5):
    t = int(input())
    L.append(t)
    S.append(int(str(t)[-1]))

ans = 0

if max(S) == 0:
    for i in range(5):
        ans += int(math.ceil(L[i] / 10) * 10)
    print(ans)
else:
    if 0 in S:
        S.remove(0)
    j = S.index(min(S))
    for i in range(5):
        if i == j:
            ans += L[i]
        else:
            ans += int(math.ceil(L[i] / 10) * 10)
    print(ans)
