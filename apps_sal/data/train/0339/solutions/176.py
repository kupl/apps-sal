from math import sqrt
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        numTwoHave = defaultdict(lambda: 0)
        numOneHave = defaultdict(lambda: 0)
        
        for j in range(len(nums2)):
            for k in range(j+1,len(nums2)):
                numTwoHave[sqrt(nums2[j]*nums2[k])] += 1
                
        for j in range(len(nums1)):
            for k in range(j+1,len(nums1)):
                numOneHave[sqrt(nums1[j]*nums1[k])] += 1
        
        #print(numOneHave)
        #print(numTwoHave)
        
        triplets = 0
        
        for num in nums1:
            if num in numTwoHave:
                triplets += numTwoHave[num]
        for num in nums2:
            if num in numOneHave:
                triplets += numOneHave[num]
            
        return triplets

