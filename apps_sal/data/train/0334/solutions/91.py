class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        import heapq
        prev = ''
        prices = []
        count = 0
        ans = 0
        for char, cost in zip(s, cost):
            if prev == char:
                heapq.heappush(prices, cost)
                count += 1
                continue
            else:
                for _ in range(count):
                    ans += heapq.heappop(prices)
                count = 0
                prev = char
                prices = [cost]
        if count != 0:
            for _ in range(count):
                    ans += heapq.heappop(prices)
        return ans
