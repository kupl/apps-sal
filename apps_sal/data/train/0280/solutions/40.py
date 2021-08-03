class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        def change(s):
            if len(s) == 1:
                return 0
            i, j = 0, len(s) - 1
            count = 0
            while i < j:
                if s[i] != s[j]:
                    count += 1
                i += 1
                j -= 1
            return count

        memo = [[-1] * (k + 1) for _ in range(len(s))]

        def dfs(s, start, k):
            if memo[start][k] != -1:
                return memo[start][k]
            if k == 1:
                memo[start][k] = change(s[start:])
                return memo[start][k]
            count = len(s) - start
            for i in range(start, len(s) - k + 1):
                print(i, k)
                count = min(count, change(s[start:i + 1]) + dfs(s, i + 1, k - 1))
            memo[start][k] = count
            return count

        return dfs(s, 0, k)
