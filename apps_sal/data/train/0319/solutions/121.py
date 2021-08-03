class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        presum = [0]
        for num in stoneValue:
            presum.append(presum[-1] + num)

        @lru_cache(None)
        def dfs(i):
            if i >= len(stoneValue):
                return 0
            ans = float('-inf')
            temp = 0
            for k in range(3):
                if i + k < len(stoneValue):
                    temp += stoneValue[i + k]
                    remain = presum[-1] - presum[i + k + 1]
                    ans = max(ans, temp + remain - dfs(i + k + 1))

            return ans

        total = dfs(0)
        if total * 2 > presum[-1]:
            return 'Alice'
        elif total * 2 < presum[-1]:
            return 'Bob'
        else:
            return 'Tie'
