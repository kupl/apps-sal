class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        listx = [sum(nums[i:j]) for i in range(0, len(nums)) for j in range(i + 1, len(nums) + 1)]
        listx.sort()
        return sum(listx[left - 1:right]) % (10 ** 9 + 7)
