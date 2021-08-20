class Solution:

    def longestStrChain(self, words: List[str]) -> int:

        def check(w1, w2):
            if len(w1) != len(w2) - 1:
                return False
            cnt = 0
            idx1 = 0
            idx2 = 0
            while idx1 < len(w1) and idx2 < len(w2) and (cnt <= 1):
                if w1[idx1] == w2[idx2]:
                    idx1 += 1
                    idx2 += 1
                else:
                    cnt += 1
                    idx2 += 1
            if cnt == 0 and idx1 == len(w1) and (idx2 == len(w2) - 1):
                return True
            elif cnt == 1 and idx1 == len(w1) and (idx2 == len(w2)):
                return True
            else:
                return False
        words.sort(key=len)
        dp = [1 for _ in range(len(words))]
        for j in range(len(words)):
            for i in range(j):
                if check(words[i], words[j]):
                    dp[j] = max(dp[j], dp[i] + 1)
        res = max(dp)
        return res
