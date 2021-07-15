from collections import *
from bisect import bisect_left as bl
import sys
input = sys.stdin.readline
def li():return [int(i) for i in input().rstrip('\n').split(' ')]
def val():return int(input())
 
for _ in range(val()):
    n = val();a = li();m = val();h = [];visited = defaultdict(int)
    for i in range(m):
        x,y = li()
        visited[x] = max(visited[x],y)
    
    endurance, currmax, h = {}, -float('inf'), sorted([[i,visited[i]] for i in visited],key = lambda x:x[0],reverse = 1)
    
    for i in range(len(h)):
        if h[i][1]>currmax:
            currmax = max(currmax,h[i][1])
            endurance[h[i][0]] = currmax
 
    power = sorted(list(endurance))

    totdays = i = 0
    while i<n:
        ind = bl(power,a[i])
        if ind == len(power):
            totdays = -1
            break
        cou = 0
        while i<n:
            while ind<len(power) and  a[i]>power[ind]:ind+=1
            if ind == len(power):
                totdays = -1;break
            if endurance[power[ind]] <= cou:break
            i+=1
            cou += 1
        if totdays == -1:break
        
        totdays += 1
    
    print(totdays)
