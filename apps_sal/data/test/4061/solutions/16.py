# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
from sys import stdin, stdout
import math
from math import gcd,sqrt

#T = int(input())
#N = int(input())
s1 = input()
N = len(s1)
s2 = input()
M = len(s2)
#print(N)
#N,M,Q = [int(x) for x in stdin.readline().split()]
#arr = [int(x) for x in stdin.readline().split()]

asc = []
dsc = []

k = 0
for i in range(len(s1)):
    if s1[i]==s2[k]:
        asc.append(i)
        k += 1
    if k==M:
        break

k = M-1
for i in range(len(s1)-1,-1,-1):
    if s1[i]==s2[k]:
        dsc.append(i)
        k -= 1
    if k==-1:
        break
        
dsc = dsc[::-1]
#print(N,M)
#print(asc,dsc)
res = 0
for i in range(M-1):
    d = dsc[i+1] - asc[i] - 1
    res = max(d,res)
    
res = max(res,asc[0])
res = max(res,dsc[0])
res = max(res,N-1-asc[-1])
res = max(res,N-1-dsc[-1])

        
print(res)

