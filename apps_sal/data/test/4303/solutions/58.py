import math
(N, K) = map(int, input().split())
cd = list(map(int, input().split()))
(cd_plus, cd_minus) = ([], [])
res = math.inf
for i in range(N):
    if cd[i] == 0:
        N -= 1
        K -= 1
        res = 0
    elif cd[i] > 0:
        cd_plus.append(cd[i])
    else:
        cd_minus.append(-cd[i])
cd_minus.sort()
for i in range(len(cd_plus)):
    if i + len(cd_minus) + 1 >= K:
        if K >= i + 2:
            res = min(res, cd_plus[i] * 2 + cd_minus[K - i - 2])
        else:
            res = min(res, cd_plus[i])
for i in range(len(cd_minus)):
    if i + len(cd_plus) + 1 >= K:
        if K >= i + 2:
            res = min(res, cd_minus[i] * 2 + cd_plus[K - i - 2])
        else:
            res = min(res, cd_minus[i])
print(res)
