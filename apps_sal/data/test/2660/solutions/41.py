"""
Created on Tue May 28 22:22:21 2019

@author: Yamazaki Kenichi
"""
import heapq
Q = int(input())
Q2 = [input() for i in range(Q)]
ans = []
(Al, Ar) = ([--(10 ** 9 + 1)], [10 ** 9 + 1])
B = 0
flg = False
for q in Q2:
    if q[0] == '1':
        (d, a, b) = list(map(int, q.split()))
        if not flg:
            heapq.heappush(Al, -a)
            B += b
            flg = True
            continue
        if len(Al) == len(Ar):
            if a < Ar[0]:
                heapq.heappush(Al, -a)
                C = abs(a - -Al[0])
            else:
                heapq.heappush(Ar, a)
                heapq.heappush(Al, -heapq.heappop(Ar))
                C = abs(a - -Al[0])
        elif a < Ar[0]:
            C = abs(a - -Al[0])
            heapq.heappush(Al, -a)
            heapq.heappush(Ar, -heapq.heappop(Al))
        else:
            C = abs(a - -Al[0])
            heapq.heappush(Ar, a)
        B += b + C
    else:
        ans.append([-Al[0], B])
for c in ans:
    print(' '.join(map(str, c)))
