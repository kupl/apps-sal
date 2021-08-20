from heapq import heapify, heappop, heappush
(x, y, a, b, c) = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
r = [-x for x in r]
p.sort()
q.sort()
r.sort()
p = p[-x:]
q = q[-y:]
heapify(p)
heapify(q)
heapify(r)
while r:
    pp = heappop(p)
    qq = heappop(q)
    rr = heappop(r)
    rr *= -1
    if pp >= rr and qq >= rr:
        heappush(p, pp)
        heappush(q, qq)
        break
    elif pp <= qq:
        heappush(q, qq)
        if pp < rr:
            heappush(p, rr)
    else:
        heappush(p, pp)
        if qq < rr:
            heappush(q, rr)
print(sum(p) + sum(q))
