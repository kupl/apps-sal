from collections import defaultdict
import heapq

class Solution:
    def isPossibleDivide(self, nums: List[int], kk: int) -> bool:
        if len(nums)%kk != 0:
            return False
        d = defaultdict(int)
        nums.sort()
        for i in nums:
            d[i] += 1
        keys = list(d.keys())
        heapq.heapify(keys)
        while len(keys) != 0:
            first = heapq.heappop(keys)
            d[first] -= 1
            if d[first] == 0:
                del d[first]
            for i in range(first+1,first+kk):
                if i not in d or d[i] <= 0:
                    return False
                d[i] -= 1
                if d[i] == 0:
                    del d[i]
                    heapq.heappop(keys)
            if d[first] > 0:
                heapq.heappush(keys,first)
        return True
                
                
        # c = 0 
        # for k in range(0,len(d),kk):
        #     if d[k] <= 0:
        #         return False
        #     if 0 < c < k and (k-1 not in d or d[k-1] <= 0):
        #         return False
        #     c += 1
        #     d[k] -= 1
        #     if c == kk:
        #         c = 0
        # return True
                
        

