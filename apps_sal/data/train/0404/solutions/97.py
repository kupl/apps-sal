class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        presum = [0] + list(itertools.accumulate(A))
        def mean(i, j):
            return (presum[j+1] - presum[i])/(j-i+1)
        n = len(A)
        old = [[mean(i, j) if i <= j else 0 for j in range(n)] for i in range(n)]
        new = [[0 for j in range(n)] for i in range(n)]
        
        mval = mean(0, n-1)
        
        for k in range(2, K+1):
            # print(f'k={k}')
            for i in range(n-k+1):
                max_val = -float('inf')
                for mid in range(i, n-k+1):
                    max_val = max(max_val, mean(i,mid) + old[mid+1][n-1])
                new[i][n-1] = max_val
            old, new = new, old
            # for x in old:
            #     print(x)
            mval = max(mval, old[0][-1])
        return mval
