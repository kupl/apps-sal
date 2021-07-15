from bisect import bisect
from collections import defaultdict

N, D, A = map(int, input().split())
XH = []

for _ in range(N):
  X, H = map(int, input().split())
  XH.append((X, -(-H//A)))

XH.sort()
Xs = [ xh[0] for xh in XH ]
HP = [ xh[1] for xh in XH ]

XR = []
for x in Xs:
  XR.append(bisect(Xs, x+2*D))

cnt = 0
temp = 0
D = defaultdict(int)

for i in range(N):
  temp -= D[i]
  HP[i] -= temp
  if HP[i] > 0:
    temp += HP[i]
    cnt += HP[i]
    D[XR[i]] += HP[i]
    HP[i] -= temp

print(cnt)
