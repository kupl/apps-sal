from collections import Counter

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        sqr_num1 = Counter(x ** 2 for x in nums1)
        sqr_num2 = Counter(x ** 2 for x in nums2)
        len_num1, len_num2 = len(nums1), len(nums2)
        multi_num1, multi_num2 = Counter(), Counter()
        
        if len_num1 > 1:
            for i in range(len_num1 - 1):
                for j in range(i + 1, len_num1):
                    multi_num1[nums1[i] * nums1[j]] += 1
                    
        if len_num2 > 1:
            for i in range(len_num2 - 1):
                for j in range(i + 1, len_num2):
                    multi_num2[nums2[i] * nums2[j]] += 1
                    
        res = 0
        
        for n in sqr_num1:
            if n in multi_num2:
                res += sqr_num1[n] * multi_num2[n]
                
        for n in sqr_num2:
            if n in multi_num1:
                res += sqr_num2[n] * multi_num1[n]
                
        return res
                
        

