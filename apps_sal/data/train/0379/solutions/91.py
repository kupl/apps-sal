class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        current_value = 0
        
        ptr1 = 0
        ptr2 = 0
        
        nums1Total = 0
        nums2Total = 0
        
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            value1 = nums1[ptr1]
            value2 = nums2[ptr2]
            
            if value1 == value2:
                current_value += max(nums1Total, nums2Total) + value1
                ptr1 += 1
                ptr2 += 1
                nums1Total = 0
                nums2Total = 0
            elif value1 < value2:
                nums1Total += value1
                ptr1 += 1
            else:
                nums2Total += value2
                ptr2 += 1
            
        while ptr1 < len(nums1):
            nums1Total += nums1[ptr1]
            ptr1 += 1
        while ptr2 < len(nums2):
            nums2Total += nums2[ptr2]
            ptr2 += 1
        
        current_value += max(nums1Total, nums2Total)
            
        return current_value % (10 ** 9 + 7)

