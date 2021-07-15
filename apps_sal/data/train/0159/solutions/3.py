from heapq import heappop
from heapq import heappush

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # -val, val, idx
        heap = []
        ans = -10001
        for i, num in enumerate(nums):
            while len(heap) > 0:
                _, val, idx = heap[0]
                if idx < i - k: # out of constraint
                    heappop(heap)
                else:
                    new_val = max(num, val + num)
                    ans = max(ans, new_val)
                    heappush(heap, (-new_val, new_val, i))
                    break
                    
            if len(heap) == 0:  # no valid previous item
                ans = max(ans, num)
                heappush(heap, (-num, num, i))
        return ans

