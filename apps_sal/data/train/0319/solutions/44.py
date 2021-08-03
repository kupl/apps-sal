class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        length = len(stoneValue)

        memo = {}

        def helper(current_idx):
            if current_idx >= length:
                return 0

            if current_idx in memo:
                return memo[current_idx]

            res = float('-inf')
            sum = 0

            for i in range(3):
                if current_idx + i < length:
                    sum += stoneValue[current_idx + i]
                    res = max(res, sum - helper(current_idx + i + 1))

            memo[current_idx] = res
            return res

        result = helper(0)

        if result == 0:
            return 'Tie'
        elif result > 0:
            return 'Alice'
        return 'Bob'
