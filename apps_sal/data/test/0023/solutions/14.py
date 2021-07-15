from functools import reduce
from fractions import gcd
import copy
from pip._vendor.distlib.compat import raw_input
import math
from decimal import *
getcontext().prec = 6

a = raw_input()
b= raw_input()
x = [None]*len(a)
y = [None]*len(b)
for i in range(len(a)):
    x[i] = int(a[i])
for i in range(len(b)):
    y[i] = int(b[i])

def zjisti(x,y):
    x.sort(reverse=True)
    c = copy.deepcopy(x)
    vysl1=[]
    if len(x)< len(y):
        v=''
        for i in range(len(x)):
            v+=(str(x[i]))
        return(v)
    if y[0] in x:
        x.remove(y[0])
        vysl1.append(y[0])
        jup = 0
        for i in range(len(y)-1):
            if y[i+1] < x[len(x)-i-1]:
                jup = -1
                break
            elif y[i+1] > x[len(x)-i-1]:
                break
        
        if jup ==0:
            o = y[0]
            y.remove(y[0])
            if len(x)>0:
                return(str(o)+zjisti(x,y))   
            else:
                return(str(o))
    q = y[0]
    for j in range(len(c)):
        if c[j]<q:
            s = c[j]
            break
    v = str(s)
    c.remove(s)
    for i in range(len(c)):
        v+=(str(c[i]))
    return(v)

print(zjisti(x,y))
