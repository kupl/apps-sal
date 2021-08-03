class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        n = len(A)
        if n < K:
            return 0
        left = 0
        right = 0
        totalCount = 0
        dp = [0 for i in range(20001)]
        result = 0

        for right in range(n):
            if dp[A[right]] == 0:
                totalCount += 1
            dp[A[right]] += 1

            while totalCount >= K:
                if totalCount == K:
                    result += 1

                dp[A[left]] -= 1
                if dp[A[left]] == 0:
                    totalCount -= 1
                left += 1

            while totalCount <= K and left > 0:
                left -= 1
                if dp[A[left]] == 0:
                    totalCount += 1
                dp[A[left]] += 1
        return result
