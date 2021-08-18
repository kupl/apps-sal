"""
Created on Tue Sep 29 15:44:49 2020

@author: liang
"""

X = int(input())

ans = 0
tmp = 0
i = 1
while True:
    tmp += i
    if tmp >= X:
        print(i)
        break
    i += 1
