class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:

        n = len(s)
        if n == 1:
            return 0
        start = 0
        end = 1
        splits = []
        while end < n:
            while end < n and s[end] == s[start]:
                end += 1
            splits.append((start, end - 1))
            start = end

        answer = 0
        for start, end in splits:
            if start == end:
                continue
            else:
                maxi = 0
                costsum = 0
                for i in range(start, end + 1):
                    maxi = max(maxi, cost[i])
                    costsum += cost[i]
                costsum -= maxi
                answer += costsum
        return answer
