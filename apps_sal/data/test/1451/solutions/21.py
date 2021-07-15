import sys
import math

def fcount(val):
    count = 0
    for i in range(len(val)):
        if(val[i] == '7' or val[i] == '4'):
            count += 1
    return count
    
n, k = [int(x) for x in (sys.stdin.readline()).split()]
ai = list((sys.stdin.readline()).split())

result = 0
for c in ai:
    if(fcount(c) <= k):
        result += 1
        
print(result)
