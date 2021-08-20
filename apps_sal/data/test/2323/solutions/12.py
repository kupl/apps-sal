import copy
import bisect
n = int(input())
s = list(map(int, input().split()))
sCopy = copy.deepcopy(s)
AP = []
mx = -1
sCopy.sort()
miss = []
for i in range(n - 1):
    mx = max(mx, sCopy[i + 1] - sCopy[i] - 1, 0)
    miss.append(max(sCopy[i + 1] - sCopy[i] - 1, 0))
miss.sort()
if miss != []:
    pSOfMiss = [miss[0]]
    for i in range(1, len(miss)):
        pSOfMiss.append(pSOfMiss[-1] + miss[i])
MAX = max(s)
MIN = min(s)
C = len(set(s))
ansList = []
mL = len(miss)
q = int(input())
for _ in range(q):
    (l, r) = list(map(int, input().split()))
    if l == r:
        ansList.append(C)
    elif n == 1:
        ans = r - l + 1
        ansList.append(ans)
    elif r - l >= mx:
        ans = MAX + r - (MIN + l) + 1
        ansList.append(ans)
    else:
        idx = bisect.bisect_right(miss, r - l)
        if idx > 0:
            notThere = pSOfMiss[-1] - pSOfMiss[idx - 1] - (r - l) * (mL - idx)
        else:
            notThere = pSOfMiss[-1] - (r - l) * (mL - idx)
        ans = MAX + r - (MIN + l) + 1 - notThere
        ansList.append(ans)
print(*ansList)
