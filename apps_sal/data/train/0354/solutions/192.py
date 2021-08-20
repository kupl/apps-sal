class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        cache = {}

        def dfs(rem, last, lastLen):
            if rem == 0:
                return 1
            if (rem, last, lastLen) in cache:
                return cache[rem, last, lastLen]
            ans = 0
            for i in range(1, 7):
                if i == last and lastLen == rollMax[i - 1]:
                    continue
                ans = (ans + dfs(rem - 1, i, 1 if i != last else lastLen + 1)) % 1000000007
            if last != -1:
                cache[rem, last, lastLen] = ans
            return ans
        return dfs(n, -1, 0)
