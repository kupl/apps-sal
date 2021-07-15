class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def helper(num):
            if num in self.dic: return self.dic[num]
            n = num
            count,even = 0,0
            while n != 0:
                if n % 2 == 1:
                    n -= 1
                else:
                    n //= 2
                    even += 1
                count += 1
            self.dic[num] = (count,even)
            return count,even
        
        ans,maxb,self.dic = 0,0,{}
        for num in nums:
            a,b = helper(num)
            ans += a - b
            maxb = max(maxb,b)
        return ans + maxb
