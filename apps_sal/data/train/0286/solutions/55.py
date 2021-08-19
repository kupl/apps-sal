class Solution:

    def getProbability(self, balls: List[int]) -> float:
        total = 0
        valid = 0

        @lru_cache(None)
        def getFactor(i):
            ans = 1
            for i in range(2, i + 1):
                ans *= i
            return ans

        def getComb(nums):
            a = getFactor(sum(nums.values()))
            duplicate = 1
            for val in nums.values():
                duplicate *= getFactor(val)
            return a // duplicate

        def dfs(i, a, b):
            nonlocal total
            nonlocal valid
            if i == len(balls):
                if sum(a.values()) != sum(b.values()):
                    return
                (p1, p2) = (getComb(a), getComb(b))
                total += p1 * p2
                if len(a) == len(b):
                    valid += p1 * p2
            else:
                for j in range(balls[i] + 1):
                    a[i] = j
                    b[i] = balls[i] - j
                    if a[i] == 0:
                        del a[i]
                    if b[i] == 0:
                        del b[i]
                    dfs(i + 1, a, b)
        dfs(0, {}, {})
        return valid / total
