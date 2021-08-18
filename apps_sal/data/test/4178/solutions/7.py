"""
Created on Thu Sep 10 00:58:18 2020

@author: liang
"""

N = int(input())
H = [0] + [int(i) for i in input().split()]
flag = True
for i in range(N):
    if H[i] - H[i + 1] >= 2:
        print("No")
        break
    if H[i] - H[i + 1] == 1:
        if flag:
            flag = False
        else:
            print("No")
            break
    if H[i] < H[i + 1]:
        flag = True

else:
    print("Yes")
