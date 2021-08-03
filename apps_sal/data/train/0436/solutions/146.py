class Solution:
    def minDays(self, n: int) -> int:
        queue = [[0, n]]
        visit = set()
        while queue:
            curr, num = heapq.heappop(queue)
            if num == 0:
                return curr
            if num not in visit:
                visit.add(num)
                if num % 3 == 0:
                    heapq.heappush(queue, [curr + 1, num // 3])
                if num % 2 == 0:
                    heapq.heappush(queue, [curr + 1, num // 2])
                heapq.heappush(queue, [curr + 1, num - 1])
