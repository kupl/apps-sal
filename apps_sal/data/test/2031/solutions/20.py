from math import *
from copy import copy
def maximum(list_ticket):
    for i in range(len(list_ticket)):
        if i == 0:
            ma=list_ticket[i]
        else:
            ma=max(ma,list_ticket[i])
    ma = list_ticket.index(ma)
    list_ticket.insert(ma,0)
    list_ticket.pop(ma+1)
    return ma

n = int(input())
a = list(map(int, input().split()))
m = int(input())
for i in range(m):
    b = copy(a)
    q = []
    array = list(map(int, input().split()))
    for i in range(array[0]):
        q.append(maximum(b))
    q.sort()
    q1 = []
    for i in range(len(q)):
        q1.append(a[q[i]])
    q1 = list(map(str, q1))
    print(q1[array[1]-1])
