from collections import deque
import heapq


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # record the best at outcome at each index

        shortest = sys.maxsize
        record = {}

        left = 0
        curr_sum = 0
        for right in range(len(arr)):
            curr_sum += arr[right]

            while curr_sum > target and left <= right:
                # shrink the window
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                # found subarray
                curr_len = right - left + 1
                prev_len = record.get(left - 1, sys.maxsize)
                record[right] = min(record.get(right - 1, sys.maxsize), curr_len)

                # update the result
                shortest = min(shortest, curr_len + prev_len)
            else:
                # keep looking
                record[right] = record.get(right - 1, sys.maxsize)

        if shortest == sys.maxsize:
            return -1

        return shortest
