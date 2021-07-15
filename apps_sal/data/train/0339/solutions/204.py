# Two sum approach

# returns the number of distinct index pairs (j, k) such that 
# array[j]*array[k] == target

from collections import defaultdict

# O(n) time, O(n) space
def two_product(array, target):
    counter = defaultdict(int)
    count = 0
    
    for index, value in enumerate(array):
        candidate = target / value
        if candidate in counter:
            count += counter[candidate]
        counter[value] += 1
    return count
    

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        count = 0
        for num in nums1:
            count += two_product(nums2, num*num)
        
        for num in nums2:
            count += two_product(nums1, num*num)
        
        return count
