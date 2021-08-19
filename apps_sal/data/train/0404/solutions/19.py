class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        # a recursive function where it gets each group from 1 to A-K2
        # the recursive function builds a tree,
        # O(K^(N-K))
        # 9, 1,2,3, 9,6,7,8 , the state = (index, K2)
        def ave(list_):
            return sum(list_) / len(list_)
        dp = {}

        def rec(index, k):
            if index == len(A):
                return 0
            if (index, k) in dp:
                return dp[(index, k)]
            if k == 1:
                return ave(A[index:])
            m = 0
            for i in range(index + 1, len(A)):
                m = max(m, ave(A[index:i]) + rec(i, k - 1))
            dp[(index, k)] = m
            return m
        return rec(0, K)
