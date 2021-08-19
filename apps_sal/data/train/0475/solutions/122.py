from itertools import accumulate
from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        cums = [0] + list(accumulate(nums))

        subsums = []
        for i in range(len(cums) - 1):
            for j in range(i + 1, len(cums)):
                subsums.append(cums[j] - cums[i])

        subsums.sort()
        # print(subsums)
        return sum(subsums[left - 1:right]) % (10**9 + 7)
