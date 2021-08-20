class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        if len(s) <= 1:
            return 0
        res = 0
        start = 0
        while True:
            if start >= len(s):
                break
            temp = start + 1
            for i in range(temp, len(s)):
                if s[i] != s[start]:
                    start += 1
                else:
                    break
            if start == len(s) - 1:
                break
            end = start + 2
            while end < len(s):
                if s[end] == s[start]:
                    end += 1
                else:
                    break
            res += sum(cost[start:end]) - max(cost[start:end])
            start = end
        return res
        '\n        start = -1\n        for i in range(1, len(s)):\n            if s[i]==s[i-1]:\n                start = i-1\n                break\n        if start==-1: return 0\n        end = start+2\n        SUM = cost[start]+cost[start+1]\n        MAX = max(cost[start], cost[start+1])\n        while end<len(s):\n            if s[end]==s[start]:\n                SUM += cost[end]\n                MAX = max(cost[end], MAX)\n                end += 1\n            else:\n                break\n        res += (SUM-MAX)\n        return res+self.minCost(s[end:], cost[end:])\n        '
