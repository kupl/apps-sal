class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1
        
        # The top of maxStack is the position of the max element currently
        # being used by the subarray.
        # As the algorithm (which grows that subarray righwards) discovers new elements that
        # are incompatible with the current max, we ditch this current max and check for validity
        # with the next max. Thus the maxStack contains a sequence of positions of the next
        # possible. This also means the values must be decreasing (think about why).
        maxStack = []
        
        # Same for minStack, but for mins.
        minStack = []
        result = 1
        
        # The subarray goes from leftPos to i.
        leftPos = 0
        for i in range(0, len(nums)):
            # if nums[i] exceeds the max, keep popping off the max and try
            # again with the next max. Naturally, we update leftPos since
            # the leftmost valid position is moving until we find a valid max
            while maxStack and nums[i] < nums[maxStack[0]] - limit:
                leftPos = max(leftPos, maxStack.pop(0) + 1)
            
            # We do the same for minimum
            while minStack and nums[i] > nums[minStack[0]] + limit:
                leftPos = max(leftPos, minStack.pop(0) + 1)
                
            length = i - leftPos + 1
            if length > result:
                result = length
                
            # recall: maxStack[0] must always be the currently used maximum. And the next elements
            # contain the next one to try if we have to ditch maxStack[0]
            # This means if nums[i] is larger than
            # ALL the elements in maxStack, then of course nums[i] should become our current max. To do
            # that we pop away the entirety of maxStack and push i onto it. But if nums[i] is larger
            # than some elements of maxStack, we pop away only those elements and then stop. Then we push
            # i to the end because it represents a possible next maximum that can be used in the future
            while maxStack and nums[i] > nums[maxStack[-1]]:
                maxStack.pop()
            maxStack.append(i)
            while minStack and nums[i] < nums[minStack[-1]]:
                minStack.pop()
            minStack.append(i)
            
        return result
