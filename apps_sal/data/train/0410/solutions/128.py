class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        nums = []
        for i in range(lo, hi + 1):
            temp, steps = i, 0
            while temp != 1:
                if temp % 2 == 0: temp //= 2
                else: temp = 3 * temp + 1
                steps += 1
            nums.append([i, steps])
        nums = sorted(nums, key=lambda n: n[1])
        return nums[k - 1][0]
