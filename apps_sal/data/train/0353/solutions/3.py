class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        ans = 0
        mod = 10 ** 9 + 7
        nums.sort()
        temp = 0
        def bina(i,low,high):
            ans = low - 1 
            while(low<=high):
                mid = (low + high)//2
                if nums[i] + nums[mid] <= target:
                    low = mid + 1
                    ans = mid
                else:
                    high = mid - 1
            return ans - i

        for i in range(len(nums)):
            if nums[i]*2 > target:
                break
            ans = (ans + int(pow( 2,bina(i,i,len(nums)-1) ,mod) ))%mod
            print(ans)
        return ans
        
        
        
                

