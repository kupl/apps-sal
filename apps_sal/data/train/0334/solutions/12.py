class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:

        H = []
        ans = 0

        i = 1
        while i < len(s):
            if i < len(s) and s[i] == s[i - 1]:
                H = []
                heapq.heappush(H, cost[i - 1])
                c = 1
                while i < len(s) and s[i] == s[i - 1]:
                    heapq.heappush(H, cost[i])
                    i += 1
                    c += 1
                while c > 1:
                    t = heapq.heappop(H)
                    ans += t
                    c -= 1
            else:
                i += 1
            H = []

        return ans
