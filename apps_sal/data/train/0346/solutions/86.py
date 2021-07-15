class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_indeces = []
        for i, elem in enumerate(nums):
            if elem % 2 != 0:
                # is odd
                odd_indeces.append(i)
        
        if len(odd_indeces) < k:
            return 0
        
        output = 0 
        
        print(odd_indeces)
        
        i = 0 
        while i + k <= len(odd_indeces): 
            first, last = odd_indeces[i], odd_indeces[i + k - 1]
            if first == 0:
                leftdist = 1
            elif i == 0:
                leftdist = first + 1
            else: 
                leftdist = odd_indeces[i] - odd_indeces[i - 1]
                
            if last == len(nums) - 1:
                rightdist = 1
            elif i + k - 1 == len(odd_indeces) - 1:
                rightdist = len(nums) - odd_indeces[i + k - 1]
            else:
                rightdist = odd_indeces[i + k] - odd_indeces[i + k - 1]
                
            output += leftdist * rightdist
                
            i += 1
        return output
                
                

