from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        sum_up_to = [0]
        total = 0
        for n in A:
            total += n
            sum_up_to.append(total)
        lsum = []
        msum = []
        for i in range(1,len(A)+1):
            if i >= L:
                lsum.append(sum_up_to[i]-sum_up_to[i-L])
            else:
                lsum.append(None)
            
            if i >= M:
                msum.append(sum_up_to[i]-sum_up_to[i-M])
            else:
                msum.append(None)
        
        max_sum = 0
        for i in range(len(lsum)):
            if lsum[i] is None:
                continue
            for j in list(range(i-L))+list(range(i+M, len(msum))):
                if msum[j] is None:
                    continue
                max_sum = max(max_sum, lsum[i]+msum[j])
        return max_sum
