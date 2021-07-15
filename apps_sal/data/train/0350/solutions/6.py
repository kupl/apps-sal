class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        from collections import Counter
        def atMost(k):
            count = Counter()
            ans = i = 0
            for j in range(len(A)):
                if not count[A[j]]:
                    k -= 1
                count[A[j]] += 1
                while k < 0:
                    count[A[i]] -= 1
                    if not count[A[i]]:
                        k += 1
                    i += 1
                ans += j - i + 1
            return ans
        return atMost(K) - atMost(K - 1)
