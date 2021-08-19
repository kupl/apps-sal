class Solution:

    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        memo = dict()

        def dp(s):
            if s >= n:
                return 0
            if s in memo:
                return memo[s]
            ans = -2 ** 31
            for i in range(1, 4):
                if s + i > n:
                    break
                ans = max(ans, sum(stoneValue[s:s + i]) - dp(s + i))
            memo[s] = ans
            return ans
        score = dp(0)
        return 'Alice' if score > 0 else 'Bob' if score < 0 else 'Tie'

    def stoneGameIII1(self, stoneValue):
        n = len(stoneValue)
        memo = dict()

        def dp(s):
            if s >= n:
                return 0
            if s in memo:
                return memo[s]
            ans = -2 ** 31
            for i in range(1, 4):
                if s + i > n:
                    break
                ans = max(ans, sum(stoneValue[s:s + i]) - dp(s + i))
            memo[s] = ans
            return ans
        score = dp(0)
        return 'Alice' if score > 0 else 'Bob' if score < 0 else 'Tie'


class Solution1:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}
        n = len(stoneValue)

        def dp(s):
            if s >= n:
                return 0
            if s in memo:
                return memo[s]
            ans = -2 ** 31
            for i in range(1, 4):
                if s + i > n:
                    break
                ans = max(ans, sum(stoneValue[s:s + i]) - dp(s + i))
            memo[s] = ans
            return ans
        score = dp(0)
        return 'Alice' if score > 0 else 'Bob' if score < 0 else 'Tie'

    def stoneGameIII2(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        cache = dict()

        def solve(s):
            if s >= n:
                return 0
            if s in cache:
                return cache[s]
            best = -2 ** 31
            presum = 0
            for x in range(1, 4):
                if s + x - 1 >= n:
                    break
                presum += stoneValue[s + x - 1]
                best = max(best, presum - solve(s + x))
            cache[s] = best
            return best
        score = solve(0)
        return 'Alice' if score > 0 else 'Bob' if score < 0 else 'Tie'
