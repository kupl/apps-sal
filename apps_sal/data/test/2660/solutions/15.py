"""
Created on Tue May 28 22:22:21 2019

@author: Yamazaki Kenichi
"""
import heapq

Q = int(input())
Q2 = [input() for i in range(Q)]

ans = []
Al, Ar = [-(-(10**9 + 1))], [10**9 + 1]
d, a, b = list(map(int, Q2[0].split()))
heapq.heappush(Al, -a)
B = b

for i in range(1, Q):
    if Q2[i][0] == '1':
        d, a, b = list(map(int, Q2[i].split()))
        if len(Al) == len(Ar):
            if a < Ar[0]:
                heapq.heappush(Al, -a)
            else:
                heapq.heappush(Ar, a)
                heapq.heappush(Al, -(heapq.heappop(Ar)))
            C = abs(a - (-Al[0]))
        else:
            C = abs(a - (-Al[0]))
            if a < Ar[0]:
                heapq.heappush(Al, -a)
                heapq.heappush(Ar, -(heapq.heappop(Al)))
            else:
                heapq.heappush(Ar, a)
        B += (b + C)
    else:
        ans.append([(-Al[0]), B])

for c in ans:
    print((' '.join(map(str, c))))
