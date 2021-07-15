from bisect import bisect_left as bl
from bisect import bisect_right as br
import heapq
import math
from collections import *
from functools import reduce,cmp_to_key
import sys
input = sys.stdin.readline
 
# M = mod = 998244353
def factors(n):return sorted(list(set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))))
# def inv_mod(n):return pow(n, mod - 2, mod)
 
def li():return [int(i) for i in input().rstrip('\n').split(' ')]
def st():return input().rstrip('\n')
def val():return int(input().rstrip('\n'))
def li2():return [i for i in input().rstrip('\n').split(' ')]
def li3():return [int(i) for i in input().rstrip('\n')]


n,L = li()
l = []
for i in range(n):
    l.append(li())

index = defaultdict(list)
for ind,i in enumerate(l):
    index[tuple(i)].append(ind + 1)
# print(index)
l.sort(key = lambda x:x[1])
d = defaultdict(list)
# print(l)

ans = i = tot = currpoints = 0
anspattern = []
he = []
# print(L)
while i < n:
    # print(l[i])
    if l[i][1] + tot <= L:
        tot += l[i][1]
        heapq.heappush(d[l[i][0]],l[i][1])
        currpoints += 1

        if len(d[l[i][0]]) == 1:
            heapq.heappush(he,l[i][0])
        # i += 1
    # print(he,d,currpoints,tot)
    while len(he) and currpoints > he[0]:
        temp = heapq.heappop(he)
        tot -= heapq.heappop(d[temp])
        currpoints -= 1
        if len(d[temp]):heapq.heappush(he,temp)
    
    if currpoints > ans:
        # print('ans change : ',ans,currpoints,anspattern)
        ans = currpoints
        # anspattern = he[:]
        # for k in he:
        #     for j in d[k]:
        #         anspattern.append(index[tuple([k,j])])
        # print('chengedans : ',ans,currpoints,anspattern)
    
        
    i += 1
i = tot = currpoints = 0
he = []
d = defaultdict(list)

while i < n:
    # print(l[i])
    if l[i][1] + tot <= L:
        tot += l[i][1]
        heapq.heappush(d[l[i][0]],l[i][1])
        currpoints += 1

        if len(d[l[i][0]]) == 1:
            heapq.heappush(he,l[i][0])
        # i += 1
    # print(he,d,currpoints,tot)
    while len(he) and currpoints > he[0]:
        temp = heapq.heappop(he)
        tot -= heapq.heappop(d[temp])
        currpoints -= 1
        if len(d[temp]):heapq.heappush(he,temp)
    
    if currpoints == ans:
        anspattern = []
        for i in he:
            for j in d[i]:
                anspattern.append(index[tuple([i,j])][-1])
                index[tuple([i,j])].pop()
        print(ans)
        print(len(anspattern))
        print(*sorted(anspattern))
        return
        # print('ans change : ',ans,currpoints,anspattern)
        ans = currpoints
        # anspattern = he[:]
        # for k in he:
        #     for j in d[k]:
        #         anspattern.append(index[tuple([k,j])])
        # print('chengedans : ',ans,currpoints,anspattern)
    
        
    i += 1
