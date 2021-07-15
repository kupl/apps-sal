class Solution:
    def getCombination( self, start, endPos):
        mod = 10**9 + 7


        #for i in range (1, qty+1):
        #    ncombination = math.factorial(qty)
        #    ncombination = ncombination/(math.factorial(i) * math.factorial(qty-i))
        #    count += ncombination
        #print (count)
        count = pow (2, endPos - start )
        return count % mod
                                         
    def findPos(self,nums,target):
        # 0 1 2,  0,1,2,3
        
        start = 0
        end = len(nums) -1
        while start <= end:

            medium = start + (end - start) // 2
            #print (start, medium, end )
            sumv = nums[0] + nums[medium]
            if sumv > target:
                # go left 
                end = medium -1
            elif sumv == target:
                if (medium == len(nums) -1) or nums[medium +1] != nums[medium]:
                    #found
                    return medium
                else:
                    # look for the rightmost
                    start = medium + 1
            else:
                #sumv < target, check rightone
                if (medium == len(nums) -1) or nums[medium +1] + nums[0] > target:
                    return medium
                else:
                    # go right
                    start = medium + 1
                
        return end 
         
            
        



    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 + 7
        nums.sort()
        #print (nums)
        #for each element, find the max
        #count the number 
        start = 0
        count = 0
        endPos = self.findPos(nums,target)
        print (endPos)
        while (start < len(nums) and start <= endPos and endPos >0):
            if nums[endPos] + nums[start] <= target:
                count += pow (2, endPos - start,mod)
                count = count % mod
                start += 1
            else:               
                endPos -= 1

        return int(count % mod)
    
    def numSubseq2(self, nums: List[int], target: int) -> int:
        nums.sort()
        left,right = 0,len(nums)-1
        res = 0
        md = 10**9+7
        while left<=right:
            if nums[left]+nums[right]<=target:
                res=(res+pow(2,right-left,md))%md
                left+=1
            else:right-=1
        return res

