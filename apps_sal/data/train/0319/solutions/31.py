class Solution:
    def stoneGameIII(self, s: List[int]) -> str:

        cost = [-1] * (len(s))

        def helper(s, i):
            if i >= len(s):
                return 0
            if cost[i] != -1:
                return cost[i]

            ans = -sys.maxsize
            ans = max(ans, s[i] - helper(s, i + 1))
            if i + 1 < len(s):
                ans = max(ans, s[i] + s[i + 1] - helper(s, i + 2))
            if i + 2 < len(s):
                ans = max(ans, s[i] + s[i + 1] + s[i + 2] - helper(s, i + 3))
            cost[i] = ans
            return cost[i]

        a = helper(s, 0)
        if a > 0:
            return 'Alice'
        if a == 0:
            return 'Tie'
        return 'Bob'
