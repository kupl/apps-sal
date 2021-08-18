"""
Created on Wed Sep  9 19:43:38 2020

@author: liang
"""

N = int(input())
H = [int(x) for x in input().split()]

ans = 0
count = 0

for i in range(N - 1):
    if H[i] >= H[i + 1]:
        count += 1
    else:
        count = 0
    if ans < count:
        ans = count
print(ans)
