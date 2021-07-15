class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        def two(target, nums):
            counter = collections.defaultdict(int)
            res = 0
            for num in nums:
                if target % num == 0:
                    res += counter[target // num]
                counter[num] += 1
            return res
                    
            
        res = 0
        for num in nums1:
            res += two(num * num, nums2)
        for num in nums2:
            res += two(num * num, nums1)
            
        return res
            
        
        
#         counter1 = collections.Counter(nums1)
#         counter2 = collections.Counter(nums2)
#         nums1 = list(set(nums1))
#         nums1.sort()
#         nums2 = list(set(nums2))
#         nums2.sort()
        
#         def helper(nums, target, counter):
            
#             res = 0
#             seen = set()
#             for num in nums:
#                 if target % num == 0:
#                     if target // num == num:
#                         res += counter[num] * (counter[num]-1) // 2
#                     elif target // num in seen:
#                         res += counter[num] * counter[target//num]
#                 seen.add(num)
#             return res
                
        
#         def findTriplets(nums1, nums2, counter1, counter2):
#             res = 0
#             for num in nums1:
#                 target = num * num
#                 res += counter1[num] * helper(nums2, target, counter2)
#             return res
        
#         res = 0
#         res += findTriplets(nums1, nums2, counter1, counter2)
#         res += findTriplets(nums2, nums1, counter2, counter1)
#         return res
                
                
        
        
                
            
            
                
                
                
        
        
        

