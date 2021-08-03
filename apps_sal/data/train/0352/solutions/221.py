class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        d = {w: 1 for w in words}
        words.sort(key=lambda x: len(x))

        def check(w1, w2):
            if len(w1) <= len(w2):
                return False
            if len(w1) - len(w2) == 1:
                '''for i in range(len(w1)):
                    temp = w1[:i] + w1[i + 1:]
                    if temp == w2:
                        return True'''
                i = 0
                j = 0
                count = 0
                while i < len(w1) and j < len(w2):
                    if w1[i] == w2[j]:
                        i += 1
                        j += 1
                    else:
                        i += 1
                        count += 1

                if count > 1:
                    return False
                else:
                    return True

            return False

        dp = [0 for _ in range(len(words))]

        dp[0] = 1
        res = 1
        for i in range(1, len(words)):
            curr_max = 0
            for j in range(i):
                if check(words[i], words[j]):
                    curr_max = max(curr_max, dp[j])

            dp[i] = curr_max + 1
            res = max(res, dp[i])

        return res
