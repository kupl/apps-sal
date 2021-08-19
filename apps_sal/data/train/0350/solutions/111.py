class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        def atMost(A: List[int], K: int):
            cache = collections.Counter()
            (res, i) = (0, 0)
            for j in range(len(A)):
                cache[A[j]] += 1
                while len(cache) > K:
                    cache[A[i]] -= 1
                    if cache[A[i]] == 0:
                        del cache[A[i]]
                    i += 1
                res += j - i + 1
            return res
        return atMost(A, K) - atMost(A, K - 1)
