class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        curr_sum = 0
        s_sum = []
        s_ind = []
        res = math.inf
        for i, num in enumerate(A):
            curr_sum += num
            while s_sum and s_sum[-1] >= curr_sum:
                s_sum.pop()
                s_ind.pop()
            
            if not s_sum:
                if curr_sum >= K:
                    res = min(res, i + 1)
            else:
                ind = bisect_right(s_sum, curr_sum - K)
                if ind - 1 >= 0:
                    res = min(res, i - s_ind[ind - 1])
                elif curr_sum >= K:
                    res = min(res, i + 1)
            
            s_sum.append(curr_sum)
            s_ind.append(i)
        
        return -1 if math.isinf(res) else res
