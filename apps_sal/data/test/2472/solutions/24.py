"""
Created on Wed Sep 16 12:27:12 2020

@author: liang
"""
N = int(input())
W = list()
for i in range(N):
    (a, b) = map(int, input().split())
    W.append((a, b))
W.sort(key=lambda x: x[1])
res = 0
for i in range(N):
    res += W[i][0]
    if res > W[i][1]:
        print('No')
        break
else:
    print('Yes')
