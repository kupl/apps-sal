class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        while True:
            i = 0
            zc = 0
            while i < n:
                if (nums[i]&1) > 0:
                    break
                elif nums[i] == 0:
                    zc += 1
                i+=1
            if zc == n:
                return res
            if i == n:
                for j in range(n):
                    nums[j] = nums[j]//2
                res+=1
            for j in range(i,n):
                if nums[j]&1:
                    nums[j]-=1
                    res+=1
