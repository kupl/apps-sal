class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        segment = [0] * len(arr)
        count = {}
        res = -1
        for i in range(len(arr)):
            (left, right) = (0, 0)
            index = arr[i] - 1
            if index - 1 >= 0:
                left = segment[index - 1]
            if index + 1 < len(arr):
                right = segment[index + 1]
            segment[index - left] = left + right + 1
            segment[index + right] = left + right + 1
            if left in count and count[left] != 0:
                count[left] -= 1
            if right in count and count[right] != 0:
                count[right] -= 1
            if left + right + 1 in count:
                count[left + right + 1] += 1
            else:
                count[left + right + 1] = 1
            if m in count and count[m] != 0:
                res = i + 1
        return res
