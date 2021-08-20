class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        ans = [[-1000000000.0] * n for i in range(n)]
        for i in range(n):
            for j in range(i + 1):
                ans[i][j] = max((ans[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0) + satisfaction[i] * (j + 1), ans[i - 1][j])
        answer = max(ans[-1])
        return answer if answer > 0 else 0
