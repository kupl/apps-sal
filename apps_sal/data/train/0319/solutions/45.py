class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        (first, second) = self.memo_search(0, stoneValue, {})
        if first > second:
            return 'Alice'
        if first == second:
            return 'Tie'
        return 'Bob'

    def memo_search(self, pos, stoneValue, memo):
        if pos in memo:
            return memo[pos]
        if pos == len(stoneValue):
            return (0, 0)
        ans = -sys.maxsize
        value = 0
        for i in range(3):
            if pos + i < len(stoneValue):
                value += stoneValue[pos + i]
                (second, first) = self.memo_search(pos + i + 1, stoneValue, memo)
                total = first + second + value
                if first + value > ans:
                    ans = first + value
        memo[pos] = (ans, total - ans)
        return (ans, total - ans)
