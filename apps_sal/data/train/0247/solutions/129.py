class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        minlens = [float('inf')] * n
        res = float('inf')
        sum1 = 0
        s = 0
        min_len = float('inf')
        for e in range(n):
            sum1 += arr[e]
            while sum1 > target:
                sum1 -= arr[s]
                s += 1
            if sum1 == target:
                cur_len = e - s + 1
                if s > 0 and minlens[s - 1] != float('inf'):
                    res = min(res, cur_len + minlens[s - 1])
                min_len = min(min_len, cur_len)
            minlens[e] = min_len
        if res != float('inf'):
            return res
        return -1
