class MinMaxList(object):

    def __init__(self):
        self._container = {}
        self._max = -6665677
        self._min = 6665677

    def min_val(self) -> int:
        return self._min

    def max_val(self) -> int:
        return self._max

    def append_val(self, val: int):
        if val in self._container:
            self._container[val] = self._container[val] + 1

        else:
            self._container[val] = 1

        self._max = max(val, self._max)
        self._min = min(val, self._min)

    def remove_val(self, val: int):
        if val in self._container:
            if self._container[val] > 1:
                self._container[val] = self._container[val] - 1
                return
            else:
                del self._container[val]

        if self._max == val:
            self._max = max(self._container.keys())

        if self._min == val:
            self._min = min(self._container.keys())


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        diff = 0
        max_result = 0
        max_subarray = 0
        low = 0
        high = 0
        window = MinMaxList()
        while high < len(nums):
            window.append_val(nums[high])
            high = high + 1
            max_subarray = max_subarray + 1
            diff = abs(window.max_val() - window.min_val())

            while diff > limit:
                window.remove_val(nums[low])
                low = low + 1
                max_subarray = max_subarray - 1
                diff = abs(window.max_val() - window.min_val())

            max_result = max(max_subarray, max_result)

        return max_result
