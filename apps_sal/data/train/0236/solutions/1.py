class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:

        if not S:
            return 0

        n = len(S)
        if n == 1:
            return 0

        total_1s = 0
        total_0s = 0
        for char in S:
            if char == '1':
                total_1s += 1
            else:
                total_0s += 1

        if total_1s == 0 or total_0s == 0:
            return 0

        prefix_sum = 0
        ans = float('inf')
        for i in range(n):
            prefix_sum += 1 if S[i] == '1' else 0
            ans = min(ans, prefix_sum + ((n - i - 1) - (total_1s - prefix_sum)))
        return min(ans, total_0s, total_1s)
