class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        n1 = len(nums1)
        n2 = len(nums2)
        
        nums1_product = defaultdict(int)
        nums2_product = defaultdict(int)
        
        # count pairs for product
        for i in range(n1-1):
            for j in range(i+1, n1):
                nums1_product[(nums1[i] * nums1[j])] += 1
        
        for i in range(n2-1):
            for j in range(i+1, n2):
                nums2_product[(nums2[i] * nums2[j])] += 1
        
        for num1 in nums1:
            target = num1 ** 2
            
            ans += nums2_product[target]
        
        for num2 in nums2:
            target = num2 ** 2
            
            ans += nums1_product[target]
  
        return ans
