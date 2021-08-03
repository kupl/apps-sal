class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @lru_cache(None)
        def dp(cur):
            if cur == len(stoneValue) - 1:
                return stoneValue[cur]
            if cur >= len(stoneValue):
                return 0
            ret = float('-inf')
            s = 0
            for i in range(3):
                # if cur + i + 1 >= len(stoneValue):
                #     break
                nxt = dp(cur + i + 1)
                s += stoneValue[cur + i] if cur + i < len(stoneValue) else 0
                ret = max(ret, s - nxt)
            # print(cur, ret)
            return ret

        ans = dp(0)
        if ans > 0:
            return 'Alice'
        elif ans < 0:
            return 'Bob'
        else:
            return 'Tie'
