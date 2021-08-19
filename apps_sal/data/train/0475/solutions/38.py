class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        new_n = []
        count = 0
        for i in range(n + 1):
            for j in range(i + 1, n + 1):
                new_n.append(sum(nums[i:j]))
        new_n.sort()
        return sum(new_n[left - 1:right]) % (10 ** 9 + 7)
