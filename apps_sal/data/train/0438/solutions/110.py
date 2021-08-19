class Solution:

    def isSorted(self, arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        return True

    def findLatestStep(self, arr: List[int], m: int) -> int:
        length = len(arr)
        if m == length:
            return m
        if self.isSorted(arr):
            return m
        binary = [0] * (len(arr) + 2)
        latest_step = -1
        for step in range(length):
            pos = arr[step]
            binary[pos] = 1
            left_len = binary[pos - 1]
            right_len = binary[pos + 1]
            new_len = left_len + right_len + 1
            if left_len == m or right_len == m:
                latest_step = step
            binary[pos - left_len] = new_len
            binary[pos + right_len] = new_len
        return latest_step
