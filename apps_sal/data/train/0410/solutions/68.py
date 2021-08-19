class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        nums = list(range(lo, hi + 1))
        count = 0
        while True:
            for i in range(len(nums)):
                if nums[i] == 0:
                    continue
                elif nums[i] == 1:
                    count += 1
                    nums[i] = 0
                    if count == k:
                        return lo + i
                elif nums[i] % 2 == 0:
                    nums[i] = nums[i] // 2
                else:
                    nums[i] = 3 * nums[i] + 1
                if nums[i] == 1:
                    count += 1
                    nums[i] = 0
                    if count == k:
                        return lo + i
