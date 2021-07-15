class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        
        self.max_sum = float('-inf')
        self.dic = {}
        
        # @functools.lru_cache(None)
        def getSum(i):
            
            if i>=len(A):
                # if cur_sum>self.max_sum:
                #     self.max_sum = cur_sum
                return 0
            if i in self.dic:
                return self.dic[i]
            cur_max = A[i]
            ret = cur_max + getSum(i+1)
            for j in range(1,K):
                if i+j<len(A):
                    if A[i+j]>cur_max:
                        cur_max = A[i+j]
                    ret = max(cur_max*(j+1) + getSum(i+j+1), ret)
                else:
                    break
            self.dic[i] = ret
            return ret
        
        return getSum(0)

                
                
        
                

