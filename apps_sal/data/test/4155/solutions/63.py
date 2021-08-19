"""
Created on Tue Sep 15 00:43:39 2020

@author: liang
"""
N = int(input())
H = [int(x) for x in input().split()]
ans = 0
for i in range(max(H)):
    count = 0
    flag = False
    for j in range(N):
        if i < H[j]:
            if flag == False:
                count += 1
            flag = True
        else:
            flag = False
    ans += count
print(ans)
