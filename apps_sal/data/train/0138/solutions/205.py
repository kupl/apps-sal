class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        #reduce to simpler problem:
        # if all elems are positive, then entire array is sol as long as thy're >= 1
        
        # an even number of negative vals still gives a pos result
        
        # insight: we don't care what the values actually are , just whether they're pos, 0 , or neg
        # insight: we can't include a zero, since the prod becomes 0, and 0 isn't +ve
        
        # idea: start with first char, if you hit zero, stop, if not, keep going, and track latest position of even number of negatives.
        
        # also start at other negative vals, and positive vals after zero.
        
#         cur_max = 0
        
#         last_even_neg = -1
        
#         for i, n in enumerate(nums):
#             if n == 0:
#                 if last_even_neg >
#             if i == 0 or (i and nums[i-1] == 0)

        # first, split the array into segment to get rid of zeros.
        
        def max_len(nums):
            negs = [i for i, x in enumerate(nums) if x < 0]
            n = len(nums)
            
            if len(negs) % 2 == 0:  # even num of odd nums, whose product is pos
                return n
            else:  # at least one neg val
                return max(n - (negs[0] + 1), negs[-1])  # exclude either left or right most neg val
            
        
        from copy import deepcopy
        chunks = []
        
        chunk = []
        for x in nums:
            if x == 0 and chunk:  # see a zero, add a new segment
                chunks.append(deepcopy(chunk))
                chunk.clear()
            elif x:
                chunk.append(x)
        chunks.append(chunk)
        print(chunks)
                
        return max(map(max_len, chunks))
