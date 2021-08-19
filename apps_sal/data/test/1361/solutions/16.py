"""
Created on Dec 17, 2014

@author: Yehiaaa
"""
input()
x = [int(n) for n in input().split()]
t = len(x) - 1
mi = 10000000000000
for i in range(1, t):
    mins = 0
    temp2 = 0
    for j in range(t):
        if j + 1 == i:
            mins = x[j + 2] - x[j]
        elif i != j:
            mins = x[j + 1] - x[j]
        temp2 = max(mins, temp2)
    mi = min(mi, temp2)
print(mi)
