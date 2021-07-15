class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        best_i = 0 
        res = 0
        for i, v in enumerate(A):
            res = max(res, v-i+best_i)
            best_i = max(best_i, v+i)
        return res

        return res
        # best_i = 0
        # res = 0 
        # for i, v in enumerate(A):
        #     res = max(res, v-i+best_i)
        #     best_i = max(best_i, v+i)
        # return res
        # best_i = 0
        # res = 0 
        # for i, v in enumerate(A):
        #     res = max(res, v- i + best_i)
        #     best_i = max(best_i, v+i)
        # return res

