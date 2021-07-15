from collections import deque
import copy

N, K, C = list(map(int,input().split()))
S = input().split()[0]
TW = 0
q = []

for s in range(len(S)):
    if S[s] == 'o':
        q.append(s+1)

WD = []
LD = 0

for s in q:
    if len(WD) > K:
        break
    if LD == 0:
        WD.append(s)
        LD = s
    elif s-LD <= C:
        continue
    else:
        WD.append(s)
        LD = s


WDR = []
LD = 0
q.reverse()

for s in q:
    if len(WDR) > K:
        break
    if LD == 0:
        WDR.append(s)
        LD = s
    elif LD - s <= C:
        continue
    else:
        WDR.append(s)
        LD = s


for d in range(len(WD)):
    if WD[d] == WDR[len(WD)-d-1]:
        print((WD[d]))


