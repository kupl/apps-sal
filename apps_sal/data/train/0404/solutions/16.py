class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        presum = [0] + list(itertools.accumulate(A))
        def mean(i, j):
            return (presum[j+1] - presum[i])/(j-i+1)
        
        max_val = [0]
        def helper(i, j, k):
            if (i, j, k) in check:
                result = check[(i, j, k)]
            elif k == 1:
                result = mean(i, j)
            else:
                result = -float('inf')
                for mid in range(i, j):
                    result = max(result, mean(i, mid) + helper(mid+1, j, k-1))
            check[(i, j, k)] = result
            max_val[0] = max(max_val[0], result)
            return result
        n = len(A)
        check = {}
        helper(0, n-1, K)
        return max_val[0]
