import heapq
(n, k) = list(map(int, input().strip().split()))
p = list(map(int, input().strip().split()))
c = list(map(int, input().strip().split()))
p = sorted([(x, i) for (i, x) in enumerate(p)], key=lambda x: x[0])
ans = []
top_k = []
cur_gold = 0
for (i, t) in enumerate(p):
    if k == 0:
        ans.append((c[t[1]], t[1]))
    elif i < k:
        cur_gold += c[t[1]]
        ans.append((cur_gold, t[1]))
        heapq.heappush(top_k, c[t[1]])
    else:
        smallest = heapq.nsmallest(1, top_k)[0]
        if smallest < c[t[1]]:
            cur_gold += c[t[1]]
            ans.append((cur_gold, t[1]))
            heapq.heappop(top_k)
            heapq.heappush(top_k, c[t[1]])
            cur_gold -= smallest
        else:
            ans.append((cur_gold + c[t[1]], t[1]))
ans = sorted(ans, key=lambda x: x[1])
print(' '.join(map(lambda x: str(x[0]), ans)))
