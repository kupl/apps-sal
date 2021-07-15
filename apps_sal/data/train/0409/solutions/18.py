class Solution:  
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        def kadane(nums):
            local_max = nums[0]
            ans = local_max
            for i in range(1,len(nums)):
                local_max = max(nums[i],local_max+nums[i])
                if (ans<local_max): ans = local_max
            return ans if ans>0 else 0
        normal = kadane(arr)
        if k==1: return normal
        tot = sum(arr)
        a = []
        for i in range(2):
            for j in range(n):
                a.append(arr[j])
        mod = 10**9+7
        temp = kadane(a)
        tot = max(0,tot)
        return max(normal,temp,tot*(k-2)+temp)%mod
