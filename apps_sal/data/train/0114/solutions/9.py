from collections import *
from bisect import bisect_left as bl
import sys
input = sys.stdin.readline
 
 
def li():return [int(i) for i in input().rstrip('\n').split(' ')]
def st():return input().rstrip('\n')
def val():return int(input())
def stli():return [int(i) for i in input().rstrip('\n')]
 
 
 
 
for _ in range(val()):
    n = val()
    a = li()
    # print(a)
    m = val()
    h = []
    visited = defaultdict(int)
    for i in range(m):
        x,y = li()
        visited[x] = max(visited[x],y)
    h = []
    for i in visited:
        h.append([i,visited[i]])
    h.sort(reverse = 1)
    endurance = {}
    m = len(h)
    currmax = -float('inf')
    for i in range(m):
        if h[i][1]>currmax:
            currmax = max(currmax,h[i][1])
            endurance[h[i][0]] = currmax
        
 
    power = sorted(list(endurance))
    # print(power,endurance)
    totdays = 0
    i = 0
    while i<n:
        ind = bl(power,a[i])
        if ind == len(power):
            totdays = -1
            break
 
        cou = 0
        while i<n:
            while ind<len(power) and  a[i]>power[ind]:
                ind+=1
            if ind == len(power):
                totdays = -1
                break
            if endurance[power[ind]] <= cou:
                break
            i+=1
            cou += 1

        if totdays == -1:break
        totdays += 1
    print(totdays)
