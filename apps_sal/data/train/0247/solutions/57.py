class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        length = len(arr)
        cumulative = [0] * length
        reverse_cumulative = [0] * length
        s = 0
        sr = 0
        for i in range(length):
            s = s + arr[i]
            cumulative[i] = s
            sr += arr[length - 1 - i]
            reverse_cumulative[i] = sr
        d = {0: -1}
        dr = {0: -1}
        forward_vals = [math.inf] * length
        backward_vals = [math.inf] * length
        best1 = math.inf
        best2 = math.inf
        i = 0
        while i < length:
            d[cumulative[i]] = i
            dr[reverse_cumulative[i]] = i
            if cumulative[i] - target in d:
                l = i - d[cumulative[i] - target]
                best1 = min(best1, l)
            forward_vals[i] = best1
            if reverse_cumulative[i] - target in dr:
                l = i - dr[reverse_cumulative[i] - target]
                best2 = min(best2, l)
            backward_vals[i] = best2
            i += 1
        best1 = math.inf
        for i in range(len(forward_vals) - 1):
            best1 = min(best1, forward_vals[i] + backward_vals[length - 2 - i])
        if best1 == math.inf:
            return -1
        return best1
