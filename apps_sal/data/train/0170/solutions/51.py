class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        def helper(i, j):
            if i < 0 or j >= len(arr):
                return 0
            if arr[i] > arr[j]:
                return min(helper(i - 1, j), helper(i, j + 1)) + 1
            return 0
        intervals = []
        start = 0
        end = 1
        while end < len(arr):
            if arr[end] >= arr[end - 1]:
                end += 1
            else:
                intervals.append((start, end))
                start = end
                end = start + 1

        if start != len(arr):
            intervals.append((start, end))

        if len(intervals) < 2:
            return 0
        result = intervals[-1][0] - intervals[0][1]
        return result + helper(intervals[0][1] - 1, intervals[-1][0])
