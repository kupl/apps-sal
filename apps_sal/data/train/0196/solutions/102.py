class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        negateA = [-x for x in A]
        print(negateA)
        cursum = 0
        res = float('-inf')
        for v in negateA:
            cursum = max(v, cursum + v)
            res = max(res, cursum)
        print(res)
        res1 = float('-inf')
        cursum = 0
        for v in A:
            cursum = max(v, cursum + v)
            res1 = max(res1, cursum)
        print(res1)
        return max(res1, sum(A) + res) if res1 > 0 else res1
