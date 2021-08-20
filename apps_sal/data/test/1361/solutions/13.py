"""
Created on ١٧\u200f/١٢\u200f/٢٠١٤

@author: mohamed265
"""
input()
t = [int(x) for x in input().split()]
n = len(t) - 1
temp = 1000000000
for i in range(1, n):
    temp2 = 0
    for j in range(n):
        if j + 1 == i:
            temp2 = max(temp2, t[j + 2] - t[j])
        elif i != j:
            temp2 = max(temp2, t[j + 1] - t[j])
    temp = min(temp, temp2)
print(temp)
