import sys
from heapq import heappop, heappush

reader = (line.rstrip() for line in sys.stdin)
input = reader.__next__
 
t = int(input())
for _ in range(t):
    n = int(input())
    mp = []
    for i in range(n):
        mi, pi = list(map(int, input().split()))
        mp.append((mi, pi))
    mp.sort()
    
    prices = []
    cost = 0
    bribed = 0
    i = n - 1
    while i >= 0:
        currM = mp[i][0]
        heappush(prices, mp[i][1])
        while i >= 1 and mp[i-1][0] == currM:
            i -= 1
            heappush(prices, mp[i][1])
        already = i + bribed
        for k in range(max(0, currM - already)):
            cost += heappop(prices)
            bribed += 1
        i -= 1
    
    print(cost)

