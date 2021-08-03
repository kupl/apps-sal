class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        memo = {}

        def helper(i, total):
            if i >= n:
                return 0
            elif (i) in memo:
                return memo[i]
            res = -math.inf
            for x in range(1, min(4, n - i + 1)):
                s = sum(stoneValue[i:i + x])
                res = max(res, total - helper(i + x, total - s))
            memo[i] = res
            return res

        total = sum(stoneValue)
        a = helper(0, total)
        b = total - a
        if a == b:
            return 'Tie'
        elif a > b:
            return 'Alice'
        else:
            return 'Bob'
