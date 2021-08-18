"""
Created on Thu Sep 10 14:46:16 2020

@author: liang
"""

N = int(input())
d = [int(x) for x in input().split()]
d.sort()
ans = d[N // 2] - d[N // 2 - 1]
print(ans)
