class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        n = len(A)
        hashmap = {}
        l = 0
        count = 0
        ans = 0
        sums = 1
        for r in range(n):
            if A[r] in hashmap:
                hashmap[A[r]] += 1
            else:
                hashmap[A[r]] = 1
            if hashmap[A[r]] == 1:
                count += 1
            while count > K or hashmap[A[l]] > 1:
                if count > K:
                    sums = 1
                else:
                    sums += 1
                hashmap[A[l]] -= 1
                if hashmap[A[l]] == 0:
                    count -= 1
                l += 1
            if count == K:
                ans += sums
        return ans
