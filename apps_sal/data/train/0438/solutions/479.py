class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = max(arr)
        dp = [1] * n
        steps = n
        if m == n:
            return steps

        for a in reversed(arr):
            steps -= 1
            i = a - 1
            dp[i] = 0
            j = i + 1
            cnt = 0
            while j < n and dp[j] == 1:
                cnt += 1
                if cnt > m:
                    break
                j += 1
            else:
                if cnt == m:
                    return steps
            j = i - 1
            cnt = 0
            while j >= 0 and dp[j] == 1:
                cnt += 1
                if cnt > m:
                    break
                j -= 1
            else:
                if cnt == m:
                    return steps
        return -1
