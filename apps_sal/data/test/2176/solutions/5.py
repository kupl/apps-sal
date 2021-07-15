# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
from sys import stdin, stdout
from collections import defaultdict
import math
import copy
 
#T = int(input())
N = int(input())
#s = input()
#N,M = [int(x) for x in stdin.readline().split()]
#arr = [int(x) for x in stdin.readline().split()]
 
permu = [0]*N
permu[0] = 1
for i in range(1,N):
    permu[i] = (permu[i-1]*(i+1))%998244353

data = []
pair = {}
for i in range(N):
    a,b = [int(x) for x in stdin.readline().split()]
    data.append((a,b))
    if a not in pair:
        pair[a] = []
        
    pair[a].append(b)
    
    
freq_one = {}
for i in range(N):
    a = data[i][0]
    if a not in freq_one:
        freq_one[a] = 1
    else:
        freq_one[a] += 1
        
all = permu[-1]

# first column
p1 = 1
for key in freq_one:
    f = freq_one[key]
    p1 *= permu[f-1]
    p1 = p1%998244353

freq_two = {}
for i in range(N):
    a = data[i][1]
    if a not in freq_two:
        freq_two[a] = 1
    else:
        freq_two[a] += 1
        
# second column        
p2 = 1
for key in freq_two:
    f = freq_two[key]
    p2 *= permu[f-1]
    p2 = p2%998244353
    
# both sorted
max_second = 0
P = list(pair.keys())
P.sort()

p3 = 1
for key in P:
    #print(key)
    mini = min(pair[key])
    if mini<max_second:
        p3 = 0
        break
    
    f = {}
    for a in pair[key]:
        if a not in f:
            f[a] = 1
        else:
            f[a] += 1
            
    p = 1
    for num in f:
        fr = f[num]
        p *= permu[fr-1]
        p = p%998244353
        
    p3 *= p
    p3 = p3%998244353
    
    max_second = max(pair[key])
    
ans = (all-p1-p2+p3)%998244353

print(ans)


    


