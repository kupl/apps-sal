import numpy
import heapq
import re
import sys
import bisect


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        left -= 1
        prefix_sum = []
        for i in range(0, len(nums)):
            tmp = []
            sum = 0
            for j in range(i, len(nums)):
                sum = sum + nums[j]
                tmp.append(sum)

            prefix_sum.append(tmp)

        hq = []
        index_arr = []
        for i in range(len(prefix_sum)):
            index_arr.append(0)
            heapq.heappush(hq, (prefix_sum[i][0], i))

        for i in range(left):
            value, index = heapq.heappop(hq)

            index_arr[index] += 1
            if index_arr[index] < len(prefix_sum[index]):
                heapq.heappush(hq, (prefix_sum[index][index_arr[index]], index))

        sum = 0
        module = int(pow(10, 9) + 7)
        for i in range(left, right):
            value, index = heapq.heappop(hq)
            sum += value
            sum %= module
            index_arr[index] += 1
            if index_arr[index] < len(prefix_sum[index]):
                heapq.heappush(hq, (prefix_sum[index][index_arr[index]], index))

        return sum
