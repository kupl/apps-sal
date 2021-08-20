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

    def findLatestStepNaive2(self, arr: List[int], m: int) -> int:
        length = len(arr)
        if m == length:
            return m
        if self.isSorted(arr):
            return m
        binary = [1] * len(arr)
        for step in range(length - 1, m - 1, -1):
            pos = arr[step] - 1
            binary[pos] = 0
            left_len = 0
            right_len = 0
            for i in range(pos - 1, -1, -1):
                if binary[i]:
                    left_len += 1
                else:
                    break
            for i in range(pos + 1, length):
                if binary[i]:
                    right_len += 1
                else:
                    break
            if left_len == m or right_len == m:
                return step
        return -1

    def findLatestStepNaive(self, arr: List[int], m: int) -> int:
        length = len(arr)
        if m == length:
            return m
        if self.isSorted(arr):
            return m
        binary = [1] * len(arr)
        for step in range(length - 1, m - 1, -1):
            binary[arr[step] - 1] = 0
            current_group_len = 0
            max_group_len = 0
            for j in range(length):
                if binary[j]:
                    current_group_len += 1
                elif current_group_len > 0:
                    if current_group_len == m:
                        return step
                    max_group_len = max(max_group_len, current_group_len)
                    current_group_len = 0
            if current_group_len == m:
                return step
            max_group_len = max(max_group_len, current_group_len)
            if max_group_len < m:
                return -1
        return -1
