class Solution:
    def minDays(self, n: int) -> int:
        q = [(0,n)]
        visited = set()
        while q:
            x, curr = heapq.heappop(q)
            if curr==1: return x+1
            if curr not in visited:
                visited.add(curr)
                heapq.heappush(q,(x+1+curr%2, curr//2))
                heapq.heappush(q,(x+1+curr%3, curr//3))
        return n

