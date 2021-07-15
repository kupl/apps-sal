class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # count all ones in binary representation
        # count length of max number (number of double operation)
        ones=0
        maxLength=0
        for x in nums:
            x=bin(x)[2:]
            maxLength=max(maxLength,len(x))
            ones+=x.count('1')
        
        print((ones,maxLength-1))
        
        return ones+maxLength-1
            
            

