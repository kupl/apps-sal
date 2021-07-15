class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(A, k):
            res = i = 0
            for j in range(len(A)):
                k -= A[j] % 2
                while k < 0:
                    k += A[i] % 2
                    i += 1
                res += j - i + 1
            return res

        return atMost(nums, k) - atMost(nums, k - 1)
