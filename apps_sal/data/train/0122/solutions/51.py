from functools import lru_cache
import sys
from itertools import accumulate

sys.setrecursionlimit(10**5)


class Solution:
    def maxScore(self, arr: List[int], k: int) -> int:

        n = len(arr)
        pre = list(accumulate(arr))
        total = pre[-1]
        # print(f'{pre=}')
        
        if k == n:
            return total
        
        w = n-k
        result = 0 
        # print(f'{w=}')
        
        for i in range(w-1, n):
            # print(f'{i=}')
            sub_sum = total - (pre[i] - pre[i-w+1] + arr[i-w+1])
            result = max(result, sub_sum)
            
            
        return result
