class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        def atmostK(k):
            count = Counter()
            res = 0
            left = 0
            right = 0
            for right in range(len(A)):
                if count[A[right]] == 0:
                    k -= 1
                count[A[right]] += 1
                while k < 0:
                    count[A[left]] -= 1
                    if count[A[left]] == 0:
                        k += 1
                    left += 1
                res += right - left + 1
            return res
        return atmostK(K) - atmostK(K - 1)
