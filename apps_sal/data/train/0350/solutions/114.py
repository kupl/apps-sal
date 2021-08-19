class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.subarraysWithAtmostKDistinct(A, K) - self.subarraysWithAtmostKDistinct(A, K - 1)

    def subarraysWithAtmostKDistinct(self, A, K):
        (l, r, count, res) = (0, 0, 0, 0)
        hashmap = [0] * 20001
        while r < len(A):
            hashmap[A[r]] += 1
            if hashmap[A[r]] == 1:
                count += 1
            while count > K:
                hashmap[A[l]] -= 1
                if hashmap[A[l]] == 0:
                    count -= 1
                l += 1
            res += r - l + 1
            r += 1
        return res
