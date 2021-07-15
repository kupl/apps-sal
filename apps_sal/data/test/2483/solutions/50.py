ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
N,C = ma()
nn = 10**5+4
times = [[0 for i in range(nn)] for j in range(C+1)]
for i in range(N):
    s,t,c = ma()
    times[c][s] +=1
    times[c][t] -=1
for c in range(1,C+1):
    for i in range(nn-1):
        times[c][i+1] += times[c][i]

tot = [0 for i in range(nn)]
for c in range(C+1):
    for i in range(nn-1):
        tot[i] += times[c][i]
        if times[c][i] == 0 and times[c][i+1] ==1:
            tot[i] +=1
print(max(tot))

