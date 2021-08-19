class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        result = dict()
        total = len(arr)
        buffer = [-1] * total
        return self.do_find(arr, m, total, 0, buffer, result)

    def do_find(self, arr, m, total, index, buffer, result):
        if index == total:
            return -1
        arr_idx = arr[index] - 1
        if arr_idx > 0 and buffer[arr_idx - 1] != -1:
            start_idx = buffer[arr_idx - 1]
            result[arr_idx - start_idx] -= 1
        else:
            start_idx = arr_idx
        if arr_idx < total - 1 and buffer[arr_idx + 1] != -1:
            end_idx = buffer[arr_idx + 1]
            result[end_idx - arr_idx] -= 1
        else:
            end_idx = arr_idx
        new_len = end_idx - start_idx + 1
        if new_len in result:
            result[new_len] += 1
        else:
            result[new_len] = 1
        buffer[end_idx] = start_idx
        buffer[start_idx] = end_idx
        current_result = index + 1 if result.get(m, 0) > 0 else -1
        next_result = self.do_find(arr, m, total, index + 1, buffer, result)
        if next_result > 0:
            return next_result
        return current_result
