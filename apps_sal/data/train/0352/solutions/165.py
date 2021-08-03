class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        if not words:
            return 0
        n = len(words)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if self.is_predecessor(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def is_predecessor(self, str1, str2):
        if len(str1) + 1 != len(str2):
            return False
        cnt = 0
        n = len(str1)
        l1, l2 = 0, 0
        while l1 < n and l2 < n + 1:
            if cnt > 1:
                return False

            if str1[l1] != str2[l2]:
                l2 += 1
                cnt += 1
            else:
                l1 += 1
                l2 += 1

        return l1 == l2 or cnt == 1
