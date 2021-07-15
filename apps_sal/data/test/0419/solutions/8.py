# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
from sys import stdin, stdout
import math
import copy
 
#T = int(input())
#N = int(input())
s = input()
#print(N)
#N,r = [int(x) for x in stdin.readline().split()]
#arr = [int(x) for x in stdin.readline().split()]
 
N = int(s, 2)

res = 0
T = 1
while T<N:
    res += 1
    T *= 4
    
print(res)
