'''
Created on Jan 12, 2015

@author: mohamed265
'''
t = [int(x) for x in input().split()]
a = t[0]
b = t[1]
c = t[2]
d = t[3]

t1 = max ((3 * a) // 10, a - (a / 250) * c)

t2 = max ((3 * b) // 10, b - (b / 250) * d)

if t1 == t2:
    print("Tie")
elif t1 > t2:
    print("Misha")
else:
    print("Vasya")

