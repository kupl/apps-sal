class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # O(n*log(sum(nums)))
        
        
        # sum = 18, threshold = 6, left = 0, right = 3
        
        l = 1
        r = max(nums)
        while l < r:
            m = l + (r - l) // 2
            # print(l, r)
            s = sum([ceil(x/m) for x in nums])
            # print(\"sum: \", s)
            if s > threshold:
                l = m + 1
            else:
                r = m
        
        return l
                
        
        

