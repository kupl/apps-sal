from heapq import heappop, heappush
q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]
l = []
r = []
ans = 0
queonecount = 0
mid = -1
for query in queries:
    if query[0] == 1:
        queonecount += 1
        (_, a, b) = query
        ans += b
        heappush(l, -a)
        heappush(r, a)
        midl = -heappop(l)
        midr = heappop(r)
        ans += abs(midl - midr)
        heappush(l, -midr)
        heappush(r, midl)
    if query[0] == 2:
        minind = -heappop(l)
        print(minind, ans)
        heappush(l, -minind)
