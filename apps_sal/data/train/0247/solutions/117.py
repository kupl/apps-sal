class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        min_lens = [sys.maxsize] * n
        l = 0
        min_len = sys.maxsize
        prefix = 0
        ans = sys.maxsize
        for r in range(n):
            prefix += arr[r]
            while prefix > target:
                prefix -= arr[l]
                l += 1
            if prefix == target:
                cur_len = r - l + 1
                if l > 0 and min_lens[l - 1] != sys.maxsize:
                    ans = min(ans, cur_len + min_lens[l - 1])
                min_len = min(min_len, cur_len)
            min_lens[r] = min_len
        return -1 if ans == sys.maxsize else ans
