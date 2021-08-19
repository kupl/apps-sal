class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        f = [0]
        for end in range(1, len(arr) + 1):
            _local = 0
            _cur_max = 0
            for start in range(end - 1, max(0, end - k) - 1, -1):
                _cur_max = max(_cur_max, arr[start])
                _local = max(_cur_max * (end - start) + f[start], _local)
            f.append(_local)
        return f[-1]
