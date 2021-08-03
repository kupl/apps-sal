import heapq


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        stack = []
        sub_nums = []
        for i, num in enumerate(nums):
            tmp_stack = []
            if i == 0:
                stack.append(num)
                heapq.heappush(sub_nums, num)
                continue
            while stack:
                val = stack.pop()
                tmp_stack.append(val + num)
                heapq.heappush(sub_nums, val + num)
            tmp_stack.append(num)
            heapq.heappush(sub_nums, num)
            stack = tmp_stack
        idx = 0
        result = 0
        while idx < right:
            if idx < left - 1:
                idx += 1
                heapq.heappop(sub_nums)
            else:
                result += heapq.heappop(sub_nums)
                idx += 1
        return result % (10 ** 9 + 7)
