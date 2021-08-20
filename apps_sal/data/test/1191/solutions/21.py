from heapq import heapify, heappush, heappushpop
(n, k) = list(map(int, input().split()))
power = list(map(int, input().split()))
coins = list(map(int, input().split()))
knights = [i for i in range(n)]
knights.sort(key=lambda x: power[x])
cursum = 0
curcoin = []
heapify(curcoin)
res = [0] * n
for i in range(min(k, n)):
    res[knights[i]] = cursum + coins[knights[i]]
    heappush(curcoin, coins[knights[i]])
    cursum += coins[knights[i]]
for i in range(min(k, n), n):
    res[knights[i]] = cursum + coins[knights[i]]
    cursum += coins[knights[i]] - heappushpop(curcoin, coins[knights[i]])
print(*res)
