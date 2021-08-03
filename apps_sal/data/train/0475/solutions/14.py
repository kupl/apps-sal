class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        stack = []
        tempstack = []
        sorted_nums = []
        modulo_num = (10 ** 9) + 7

        for i, num in enumerate(nums):
            if i == 0:
                stack.append(num)
                continue
            else:
                while stack:
                    val = stack.pop()
                    heapq.heappush(sorted_nums, val)
                    tempstack.append(val + num)
                tempstack.append(num)
                stack = tempstack
                tempstack = []

        while stack:
            heapq.heappush(sorted_nums, stack.pop())

        start = 1
        result = 0

        while start <= right:
            if start < left:
                start += 1
                heapq.heappop(sorted_nums)
            else:
                result += heapq.heappop(sorted_nums)
                start += 1

        return result % modulo_num
