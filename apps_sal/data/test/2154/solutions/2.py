from heapq import heappush, heappop
n = int(input())
ar = list(map(int, input().split()))
unsed = []
selled = []
sm = 0
for x in ar:
    (U, S) = (len(unsed), len(selled))
    u = heappop(unsed) if U else float('inf')
    s = heappop(selled) if S else float('inf')
    y = min(u, s)
    if y < x:
        if u == y:
            sm += x - y
            if S:
                heappush(selled, s)
            heappush(selled, x)
        else:
            sm += x - y
            heappush(unsed, y)
            if U:
                heappush(unsed, u)
            heappush(selled, x)
    else:
        if S:
            heappush(selled, s)
        if U:
            heappush(unsed, u)
        heappush(unsed, x)
print(sm)
