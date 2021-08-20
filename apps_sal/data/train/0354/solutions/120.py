class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        self.ans = 0

        @lru_cache(maxsize=None)
        def rec(index, k, num):
            if index == n:
                return 1
            ans = 0
            for i in range(6):
                if i != k:
                    ans += rec(index + 1, i, 1)
                elif num + 1 <= rollMax[i]:
                    ans += rec(index + 1, i, num + 1)
            return ans
        return rec(0, -1, 0) % (10 ** 9 + 7)
