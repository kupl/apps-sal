class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0
        words.sort(key=len)

        def isNeighbor(a, b):
            if len(a) + 1 != len(b):
                return False
            if a == b[1:] or a == b[:-1]:
                return True
            (ia, ib) = (0, 0)
            flag = True
            while ia < len(a):
                if a[ia] == b[ib]:
                    (ia, ib) = (ia + 1, ib + 1)
                elif flag:
                    flag = False
                    ib += 1
                else:
                    return False
            return True
        dp = [1] * len(words)
        ans = 0
        for i in range(len(words)):
            for j in range(i):
                if len(words[j]) + 1 < len(words[i]):
                    continue
                elif len(words[j]) + 1 > len(words[i]):
                    break
                elif isNeighbor(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(ans, dp[i])
        return ans
