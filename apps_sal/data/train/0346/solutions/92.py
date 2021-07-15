class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #双指针:循环右指针，嵌套左指针移动标准，夹杂计数。
        nums = [i%2 for i in nums]
        ans = 0
        tmp = 0
        n = len(nums)
        l = 0#左指针
        for r in range(n):
            #循环右指针
            if nums[r]==1:
                k -= 1
                tmp = 0
                
            while k == 0:
                #挪动左指针
                #print(l,r)
                k += nums[l]#踢出一个奇数即停止，重新回到右指针的循环
                l += 1
                tmp += 1
                
            
            ans += tmp
            #print(l,r,ans)
        return ans

