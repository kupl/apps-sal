class Solution:

    def subarraysDivByK(self, A: List[int], K: int) -> int:
        n = len(A)
        prefixsum = 0
        remain = collections.defaultdict(int)
        remain[0] = 1
        res = 0
        for i in range(n):
            prefixsum += A[i]
            re = prefixsum % K
            res += remain[re]
            remain[re] += 1
        return res
