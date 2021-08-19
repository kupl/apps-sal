class Solution:

    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        return self.atMost(A, S) - self.atMost(A, S - 1)

    def atMost(self, A, S):
        res = 0
        i = 0
        pre_sum = 0
        for (j, val) in enumerate(A):
            pre_sum += val
            while pre_sum > S and i <= j:
                print(pre_sum, i)
                pre_sum -= A[i]
                i += 1
            res += j - i + 1
        return res
