class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        def atMostK(k):
            count = Counter()
            ans = left = 0
            for (i, a) in enumerate(A):
                if count[a] == 0:
                    k -= 1
                count[a] += 1
                while k < 0:
                    count[A[left]] -= 1
                    if count[A[left]] == 0:
                        k += 1
                    left += 1
                ans += i - left + 1
            return ans
        return atMostK(K) - atMostK(K - 1)
