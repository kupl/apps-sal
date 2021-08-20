"""
Created on Tue Sep 22 15:10:57 2020

@author: liang
"""
N = int(input())
lis10 = list()
lis = list()
ans = 0
for i in range(N):
    s = int(input())
    if s % 10 == 0:
        lis10.append(s)
    else:
        lis.append(s)
ans += sum(lis10)
lis.sort()
ans += sum(lis)
if ans % 10 == 0:
    if lis:
        ans -= lis[0]
    else:
        ans = 0
print(ans)
