from functools import reduce
from operator import *
from math import *
from sys import *
from string import *
from collections import *
setrecursionlimit(10**7)
dX= [-1, 1, 0, 0,-1, 1,-1, 1]
dY= [ 0, 0,-1, 1, 1,-1,-1, 1]
RI=lambda: list(map(int,input().split()))
RS=lambda: input().rstrip().split()
#################################################
val={'<':1, '>':2, '[':1, ']':2, '(':1, ')':2, '{':1, '}':2}
pairs={'<':'>', '[':']','(':')','{':'}'}
s=input()
st=[]
ans=0
for i in s:
    if len(st) and val[st[-1]]==val[i]-1:
        if pairs[st[-1]]!=i:
            ans+=1
        st.pop()
    else:
        st.append(i)
print([ans,"Impossible"][len(st)>0])

