class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.atMostK(A, K) - self.atMostK(A, K - 1)

    def atMostK(self, A, k):
        start = 0
        end = 0
        res = 0
        chars = collections.Counter()
        distinct = 0
        while end < len(A):
            if chars[A[end]] == 0:
                distinct += 1
            chars[A[end]] += 1
            while distinct > k:
                chars[A[start]] -= 1
                if chars[A[start]] == 0:
                    distinct -= 1
                start += 1
            res += end - start + 1
            end += 1
        return res
