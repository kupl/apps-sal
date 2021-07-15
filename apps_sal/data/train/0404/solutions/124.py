from itertools import combinations
from functools import lru_cache
class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        #brute force...how many ways are there to partition an array?
        # cubic time for n>>3
        # the questoin says: AT MOST K, so we could get away with K = 1
        # but K =1 is always the smallest (largest divisor in the mean)
        # I wonder if greedy would work
        def mean(A):
            return sum(A)/len(A);
        @lru_cache(None)
        def recurse(start, end, k = 1):
            if(k == K):
                return mean(A[start:end]);
            if(len(A) == 1):
                return A[0]
            maxval = 0;
            for i in range(start+1,end):
                maxval = max(maxval, mean(A[start:i])+recurse(i, end, k+1));
            return maxval
            
        # def recurse(A, k = 1):
        #     if(k == K):
        #         return mean(A);
        #     if(len(A) == 1):
        #         return A[0]
        #     N = len(A);
        #     maxval = 0;
        #     # print(A)
        #     for i in range(1,N):
        #         split1 = A[0:i]
        #         split2 = A[i:N]
        #         maxval = max(maxval, mean(split1)+recurse(split2,k+1))
        #     return maxval
                
        N = len(A)
        return recurse(0,N)
