import math
from fractions import Decimal
S = input()
N = int(input())
Srep = {}
ansrep = {}
for item in 'abcdefghijklmnopqrstuvwxyz':
    Srep[item] = 0
    ansrep[item] = 0
for item in S:
    Srep[item] += 1
    ansrep[item] += 1
Q = list(set(S))
if len(Q) > N:
    print(-1)
else:
    n = len(Q)
    ans = list(S)
    num = 1
    req = 1
    n = len(ans)
    while len(ans) > N:
        n = len(ans)
        minn = req + 1005
        removal = ans[0]
        k = True
        for item in ans:
            if ansrep[item] == 1:
                continue
            if math.ceil(Srep[item] / (ansrep[item] - 1)) > req:
                if minn > math.ceil(Srep[item] / (ansrep[item] - 1)):
                    minn = math.ceil(Srep[item] / (ansrep[item] - 1))
                    removal = str(item)
                continue
            else:
                ansrep[item] -= 1
                ans.remove(item)
                k = False
                break
        if k:
            ansrep[removal] -= 1
            req = math.ceil(Srep[removal] / ansrep[removal])
            ans.remove(removal)
    g = ''
    if len(ans) < N:
        g = S[0] * (N - len(ans))
    print(req)
    for item in ans:
        print(item, end='')
    print(g)
