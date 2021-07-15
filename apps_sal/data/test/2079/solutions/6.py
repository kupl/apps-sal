n = int(input())
W = [int(x) for x in input().split()]
W = sorted((w,i) for i,w in enumerate(W))

P = input()

smallfree = 0
smallhalf = 0
highfree = n-1
highasdk = n-1

R = []

from collections import defaultdict as dd, deque

Q = deque()

for p in P:
    if p == '0':
        R.append(W[smallfree][1])
        Q.append(smallfree)
        smallfree += 1
    else:
        seat = Q.pop()
        R.append(W[seat][1])
print(*[r+1 for r in R])



