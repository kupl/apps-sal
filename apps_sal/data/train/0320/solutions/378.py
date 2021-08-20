class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        while True:
            ok = False
            flag = True
            for i in range(n):
                if nums[i] & 1:
                    ans += 1
                    nums[i] -= 1
                if nums[i] != 0 and (not nums[i] & 1):
                    nums[i] //= 2
                    if flag:
                        ans += 1
                        flag = False
                if nums[i] != 0:
                    ok = True
            if not ok:
                break
        return ans
