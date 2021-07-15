class Solution:
    
    
    
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        self.count = 0
        
        def computeCount(nums1, nums2):
            hashMap = {}
            for i in range(len(nums1)):
                checkNum = nums1[i] ** 2
                for j in range(len(nums2)):
                    modulus = checkNum/nums2[j]
                    if modulus in hashMap:
                        self.count += hashMap[modulus]
                    if nums2[j] in hashMap:
                        hashMap[nums2[j]] += 1
                    else:
                        hashMap[nums2[j]] = 1             
                hashMap.clear()

        computeCount(nums1, nums2)
        computeCount(nums2,nums1)
        return self.count
