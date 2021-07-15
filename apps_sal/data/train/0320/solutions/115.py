import math
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=0
        maxi=0
        for j in nums:
            e=0
            if(j==0):
                continue
            if(j==1):
                count=count+1
            if(j>1):
                while(j):
                    if(j%2==0):
                        e=e+1
                        j=j//2
                    else:
                        j=j-1
                        count=count+1
            if(e>maxi):
                maxi=e
                        
        count=count+maxi
        return count
                

