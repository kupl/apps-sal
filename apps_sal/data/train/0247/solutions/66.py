class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        su = 0
        s = 0
        min_len = float('inf')
        min_lens = [float('inf') for _ in range(n)]
        ans = float('inf')
        for e in range(n):
            su += arr[e]
            while su > target:
                su -= arr[s]
                s += 1
            if su == target:
                cur_len = e - s + 1
                if s > 0 and min_lens[s - 1] != float('inf'):
                    ans = min(ans, cur_len + min_lens[s - 1])
                min_len = min(min_len, cur_len)
            min_lens[e] = min_len
        return -1 if ans >= float('inf') else ans
