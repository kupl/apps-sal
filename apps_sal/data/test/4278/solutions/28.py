"""
Created on Thu Sep 10 00:32:19 2020

@author: liang
"""

N = int(input())
d = dict()
for i in range(N):
    S = input()
    S = ''.join(sorted(list(S)))
    if S in d.keys():
        d[S] += 1
    else:
        d[S] = 1

ans = 0
for n in d.values():
    ans += n * (n - 1) // 2
print(ans)
