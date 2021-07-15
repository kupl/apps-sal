# D - String Formation
from collections import deque 
S = deque(input())
Q = int(input())
Query = [list(input().split()) for _ in range(Q)]

# 文字列の向き (0: 正, 1: 逆)
rev = 0
for Q in Query:
    if Q[0] == '1':
        if rev == 0:
            rev = 1
        else:
            rev = 0
        continue
    if Q[1] == '1':
        if rev == 0:
            S.appendleft(Q[2])
        else:
            S.append(Q[2])
    else:
        if rev == 0:
            S.append(Q[2])
        else:
            S.appendleft(Q[2])

if rev == 1:
    ans = list(reversed(list(S)))
else:
    ans = list(S)
print(''.join(ans))
