class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        prefix = [0]
        for num in A:
            prefix.append(num + prefix[-1])
        n = len(A)
        ans = 0

        for i in range(n - L + 1):
            a = prefix[i + L] - prefix[i]
            for j in range(n - M + 1):
                if j + M <= i or i + L <= j:
                    b = prefix[j + M] - prefix[j]
                    ans = max(ans, a + b)
        return ans
