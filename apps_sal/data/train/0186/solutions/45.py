class Solution:

    def largestNumber(self, cost: List[int], target: int) -> str:
        q = [(0, -target)]
        visited = {}
        costs = dict(zip(range(1, 10), cost))
        for (i, a) in enumerate(cost, 1):
            for b in cost[i:]:
                if b <= a and (not a % b):
                    del costs[i]
                    break
        while q:
            (n, hp) = heapq.heappop(q)
            n = -n
            hp = -hp
            if hp < 0:
                continue
            if visited.get(hp, -1) >= n:
                continue
            visited[hp] = n
            for c in costs:
                if costs[c] <= hp:
                    heapq.heappush(q, (-(n * 10 + c), -(hp - costs[c])))
        return str(visited.get(0, 0))
