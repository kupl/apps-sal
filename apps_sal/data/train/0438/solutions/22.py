class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if n == m:
            return n
        lengths = [0 for _ in range(n + 2)]
        last_seen = -1
        for step, i in enumerate(arr):
            left_length = lengths[i - 1]
            right_length = lengths[i + 1]
            new_length = left_length + right_length + 1
            lengths[i] = new_length
            lengths[i - left_length] = new_length
            lengths[i + right_length] = new_length
            if left_length == m or right_length == m:
                last_seen = step
        return last_seen
