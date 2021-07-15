from collections import defaultdict

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        ans = -1
        forLib = defaultdict(int)
        backLib = defaultdict(int)
        memo = {0: len(arr)}
        for i in range(len(arr)):
            index = arr[i]
            val = backLib[index - 1] + 1 + forLib[index + 1]
            if val not in memo:
                memo[val] = 0
            memo[val] += 1
            memo[backLib[index - 1]] -= 1
            memo[forLib[index + 1]] -= 1
            if val == m:
                ans = i + 1
            if (backLib[index - 1] == m or forLib[index + 1] == m) and memo[m] == 0:
                ans = i  
            forLib[index - backLib[index - 1]] = val
            backLib[index + forLib[index + 1]] = val
        return ans

