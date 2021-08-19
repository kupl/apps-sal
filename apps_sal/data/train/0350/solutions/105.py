class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        def at_most(x):
            left = 0
            counts = Counter()
            res = 0
            for (right, num) in enumerate(A):
                counts[num] += 1
                while len(counts) > x:
                    counts[A[left]] -= 1
                    if counts[A[left]] == 0:
                        del counts[A[left]]
                    left += 1
                res += right - left + 1
            return res
        return at_most(K) - at_most(K - 1)
