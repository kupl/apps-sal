class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def if_pred(a, b):
            if len(a) + 1 != len(b):
                return False
            i = 0
            j = 0
            while i < len(a):
                if a[i] == b[j]:
                    i += 1
                j += 1

                if j - i > 1:
                    return False
            else:
                return True

        words.sort(key=lambda x: len(x))
        dp = [1 for _ in range(len(words))]

        for i in range(len(words)):
            for j in range(i - 1, -1, -1):
                if if_pred(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)

        print(dp)
        return max(dp)
