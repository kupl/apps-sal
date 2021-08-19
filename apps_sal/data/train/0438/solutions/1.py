class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m
        groupLen = [0 for i in range(len(arr) + 2)]
        latestStep = -1
        for step in range(len(arr)):
            index = arr[step] - 1
            left = groupLen[index - 1]
            right = groupLen[index + 1]
            groupLen[index - left] = groupLen[index + right] = 1 + left + right
            if left == m or right == m:
                latestStep = step
        return latestStep
