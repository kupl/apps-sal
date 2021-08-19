"""
Created on Tue Sep 22 04:19:50 2020

@author: liang
"""
N = int(input())
A = [int(x) for x in input().split()]
d = [False] * 8
count = 0
ans = 0
for a in A:
    if a // 400 >= 8:
        count += 1
    elif d[a // 400] == False:
        ans += 1
        d[a // 400] = True
if count == 0:
    print(ans, ans)
elif ans == 0:
    print(1, count)
else:
    print(ans, ans + count)
