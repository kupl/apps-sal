class Solution:
    def productPresent(self, numbers , required):
        result = 0
        count = collections.defaultdict(int)
        for number in numbers:
            count[number] += 1
        
        for number in numbers:
            if required % number != 0:
                continue
            keyRequired = required // number
            if keyRequired in count and count[keyRequired] > 0:
                if keyRequired == number:
                    result += (count[keyRequired] - 1)
                else:
                    result += count[keyRequired]
            count[number] -= 1
        
        return result
                    
                    
        
        
            
            
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        for i in (nums1):
            required = i * i
            result += self.productPresent(nums2,required)
        
        for i in (nums2):
            required = i * i
            result += self.productPresent(nums1,required)
        
        return result
        
        

