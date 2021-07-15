class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def countBit(num) :
            count, highbit = 0, 0
            while num > 0:
                highbit += 1
                if num % 2 == 1:
                    count +=  1
                num //= 2
            return count, highbit
                
            
        nums = sorted(nums)
        last={}
        sum = 0
        maxDouble = 0
        for num in nums:
            if num == 0 :
                continue
            elif num in last:
                sum += last[num]
            else:
                count, highbit = countBit(num)
                maxDouble = max(maxDouble, highbit)
                sum += count
                last = {num: count}
        
        print (sum, maxDouble)
        if maxDouble == 0:
            return 0
        return sum + maxDouble - 1
