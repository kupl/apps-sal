from collections import defaultdict


class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        nums = defaultdict(int)
        for num in arr:
            nums[num] += 1
        sorted_nums = sorted(nums.items(), key=lambda x: x[1])
        tmp = k
        while tmp > 0:
            n = sorted_nums[0][1]
            if tmp < n:
                break
            tmp -= n
            sorted_nums.pop(0)
        return len(sorted_nums)
