class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        dp = [1] * (n + 1)
        res = -1
        if n == m:
            return n
        for i in range(len(arr) - 1, -1, -1):
            dp[arr[i]] = 0
            j = arr[i] + 1
            count = 0
            while j < len(dp) and dp[j] == 1:
                count += 1
                if count > m:
                    break
                j += 1
            if count == m:
                return i
            j = arr[i] - 1
            count = 0
            while j >= 1 and dp[j] == 1:
                count += 1
                if count > m:
                    break
                j -= 1
            if count == m:
                return i
        return -1
