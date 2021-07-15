class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return 0
        
        return self.helper(nums1, nums2) + self.helper(nums2, nums1)
    
    def helper(self, nums1, nums2):
        lookup = {}
        count = 0
        for num2 in nums2:
            for num1 in nums1:
                square = num1**2
                mod = square%num2
                divide = square//num2
                if square >= num2 and mod == 0 and divide in lookup:
                    count += lookup[divide]
            if num2 not in lookup:
                lookup[num2] = 0
            lookup[num2] += 1
        return count
