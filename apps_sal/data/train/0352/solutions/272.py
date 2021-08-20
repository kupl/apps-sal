class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        print(words)

        def stringmatch(s1, s2):
            onemismatchallowed = True
            if len(s1) > len(s2):
                (s2, s1) = (s1, s2)
            if len(s1) + 1 != len(s2):
                return False
            (i, j) = (0, 0)
            while i < len(s1):
                if s1[i] != s2[j]:
                    if onemismatchallowed == True:
                        onemismatchallowed = False
                    else:
                        return False
                    j += 1
                else:
                    i += 1
                    j += 1
            return True
        dp = [1 for _ in range(len(words))]
        ans = 1
        for i in range(1, len(words)):
            j = i - 1
            while j >= 0 and len(words[j]) + 1 >= len(words[i]):
                val = stringmatch(words[j], words[i])
                if val:
                    print(words[j], words[i])
                    print(dp[i])
                    dp[i] = max(dp[j] + 1, dp[i])
                    ans = max(dp[i], ans)
                j -= 1
        print(dp)
        return ans
