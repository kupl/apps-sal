"""
Created on Wed Sep 23 16:58:10 2020

@author: liang
"""


"""
【パディングはソート後】
"""
N = int(input())
A = [int(input()) for _ in range(N)]
A.sort()
A += [-1]
ans = 0
count = 1
for i in range(N):
    if A[i] == A[i + 1]:
        count += 1
    else:
        if count % 2 == 1:
            ans += 1
        count = 1
print(ans)
