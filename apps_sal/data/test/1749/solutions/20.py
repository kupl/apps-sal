import sys
from collections import defaultdict
N = []
N1 = []
M = defaultdict(int)
M1 = defaultdict(int)
(n, l, r) = list(map(int, input().split()))
N = list(map(int, input().split()))
N1 = list(map(int, input().split()))
Pass = True
for i in range(l - 1):
    if N[i] != N1[i]:
        Pass = False
        break
if Pass is True:
    for i in range(r, n):
        if N[i] != N1[i]:
            Pass = False
            break
if Pass is True:
    for i in range(l - 1, r):
        M[N[i]] += 1
        M1[N1[i]] += 1
    for i in range(n + 1):
        if M[i] != M1[i]:
            Pass = False
            break
if Pass:
    print('TRUTH')
else:
    print('LIE')
