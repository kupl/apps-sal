class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        arr_len = len(arr)
        dp = [sys.maxsize] * arr_len
        left = right = 0
        sum_tmp = 0
        length, ans_len = sys.maxsize, sys.maxsize
        while right < arr_len:
            sum_tmp += arr[right]
            while sum_tmp > target:
                sum_tmp -= arr[left]
                left += 1
            if sum_tmp == target:
                if left > 0 and dp[left-1] != sys.maxsize:
                    length = min(length, dp[left-1] + right - left + 1)
                ans_len = min(ans_len, right - left + 1)
            dp[right] = ans_len
            right += 1
        
        return length if length != sys.maxsize else -1

