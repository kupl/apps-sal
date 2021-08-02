import sys
from collections import defaultdict


N = int(input())
S = []
Subs = defaultdict(int)
for i in range(N):
    s = input()
    S.append(s)
    for ff in range(1, 10):
        for ss in range(10 - ff):
            Subs[s[ss:ss + ff]] += 1

for i in range(N):
    flag = 0
    At = S[i]
    for ff in range(1, 10):
        curr = defaultdict(int)
        for ss in range(10 - ff):
            curr[At[ss:ss + ff]] += 1
        # Here we check
        for key in list(curr.keys()):
            if(curr[key] == Subs[key]):
                print(key)
                flag = 1
                break
        if(flag):
            break
