class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort()
        ans = 0
        for i in range(n):
            coef = 0
            for k in range(1, n + 1):
                if i + k - 1 < n:
                    coef += satisfaction[i + k - 1] * k
            ans = max(ans, coef)
        return ans
