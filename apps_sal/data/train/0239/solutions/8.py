from collections import defaultdict


class Solution:
    def quickselect(self, nums, K):
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def partition(nums, left, right, pivotIdx):
            if right - left <= 1:
                return left

            pivot = nums[pivotIdx]
            swap(nums, pivotIdx, right - 1)

            read_idx = left
            write_idx = left
            while read_idx < right - 1:
                if nums[read_idx] > pivot:
                    swap(nums, read_idx, write_idx)
                    write_idx += 1
                read_idx += 1

            swap(nums, write_idx, right - 1)
            return write_idx

        left = 0
        right = len(nums)
        pivotIdx = -1
        while pivotIdx != K:
            pivotIdx = left + (right - left) // 2
            pivotIdx = partition(nums, left, right, pivotIdx)

            if pivotIdx < K:
                left = pivotIdx + 1
            elif pivotIdx > K:
                right = pivotIdx

    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        valuesByLabel = defaultdict(list)
        for value, label in zip(values, labels):
            valuesByLabel[label].append(value)

        valuesWithinLimit = []
        for i_label, i_values in valuesByLabel.items():
            self.quickselect(i_values, use_limit)
            valuesWithinLimit += i_values[:use_limit]

        self.quickselect(valuesWithinLimit, num_wanted)
        return sum(valuesWithinLimit[:num_wanted])
