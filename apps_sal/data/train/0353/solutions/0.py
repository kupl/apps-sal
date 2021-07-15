class Solution:
    MODS = 10 ** 9 + 7
    def numSubseq(self, nums: List[int], target: int) -> int:
        N = len(nums)
        cal_map = [1]
        for ii in range(1, N):
            cal_map.append(cal_map[-1] * 2 % self.MODS)
        left, right, res = 0, N - 1, 0
        nums.sort()
        while left < N:
            if nums[left] * 2 > target:
                break
            while right - 1 >= left and nums[left] > target - nums[right]:
                right -= 1
            res += cal_map[right - left]
            # print(left, right, cal_map[right - left], nums[left])
            left += 1
        return res % self.MODS
            

