import heapq

n, k = [int(x) for x in input().strip().split()]
p = [int(x) for x in input().strip().split()]
c = [int(x) for x in input().strip().split()]

a = sorted(zip(p, c, list(range(n))))
coins = []
s = 0
ans = []

for ai in a:
    s += ai[1]
    ans.append([ai[2], s])
    heapq.heappush(coins, ai[1])
    if len(coins) > k:
        s -= heapq.heappop(coins)

print(*[c for i, c in sorted(ans)])

