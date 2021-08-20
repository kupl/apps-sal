"""
Created on Wed Sep  9 01:08:27 2020

@author: liang
"""
N = int(input())
A = [int(x) for x in input().split()]
count = 1
for a in A:
    if a == count:
        count += 1
if count == 1:
    ans = -1
else:
    ans = N - count + 1
print(ans)
