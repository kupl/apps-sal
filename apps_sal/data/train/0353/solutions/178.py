class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # Number of sebsequences that satisfy given sum
        # 10:50 9/10/20

        def find_right(nums, j, target):  # len(nums)
            if j == 1:
                return j - 1
            i = 0
            while i < j:
                mid = i + (j - i) // 2
                if nums[mid] + nums[0] > target:
                    j = mid
                else:
                    i = mid + 1
            return i - 1

        n = len(nums)
        nums.sort()
        left = 0
        right = find_right(nums, len(nums), target)
        MOD = 10**9 + 7
        res = 0

        while left <= right:
            if nums[left] + nums[right] <= target:
                # res += (2**(right - left + 1)-1) % MOD
                res = (res + pow(2, right - left)) % MOD
                left += 1
            else:
                right -= 1

        return res

        # n,result,p1,p2,m=len(nums),0,0,len(nums)-1,1000000007
        # nums.sort()
        # while(p1<=p2):
        #     if nums[p1]+nums[p2]<=target:
        #         result=(result+pow(2,p2-p1,m))%m
        #         p1+=1
        #     else:
        #         p2-=1
        # return result
