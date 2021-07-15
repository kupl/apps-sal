class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        return self.check_list(nums1, nums2) + self.check_list(nums2, nums1)
        
    def check_list(self, nums1, nums2):
        count = 0
        for value in nums1:
            target = value ** 2
            count += self.find_two_sum(nums2, target)
            
        return count
            
            
    def find_two_sum(self, nums, target):
        found = dict()
        count = 0
        for idx, num in enumerate(nums):
            
            if target % num != 0:
                continue
            
            search_val = target // num
            
            if search_val in found.keys():
                count += len(found[search_val])
                
            if num in found.keys():
                found[num].append(idx)
                
            else:
                found[num] = [idx]
                
        return count
