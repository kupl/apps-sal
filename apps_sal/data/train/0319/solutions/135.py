class Solution:

    def stoneGameIII(self, s: List[int]) -> str:
        cost = [0] * (len(s) + 1)
        i = len(s) - 1
        while i >= 0:
            ans = -sys.maxsize
            ans = max(ans, s[i] - cost[i + 1])
            if i + 1 < len(s):
                ans = max(ans, s[i] + s[i + 1] - cost[i + 2])
            if i + 2 < len(s):
                ans = max(ans, s[i] + s[i + 1] + s[i + 2] - cost[i + 3])
            cost[i] = ans
            i -= 1
        a = cost[0]
        if a > 0:
            return 'Alice'
        if a == 0:
            return 'Tie'
        return 'Bob'
