from collections import defaultdict


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # idea is to sort words based on length and then apply dfs on each index
        n = len(words)
        words.sort(key=len)
        memo = {}

        def check_pred(word1, word2):
            if len(word2) - len(word1) != 1:
                return False
            for i in range(len(word2)):
                pred_str = word2[0:i] + word2[i + 1:]
                if word1 == pred_str:
                    return True
            return False

        def recur(start):
            if start in memo:
                return memo[start]
            f_max = 1
            for i in range(start + 1, n):
                c_max = 1
                if check_pred(words[start], words[i]):
                    c_max = 1 + recur(i)
                f_max = max(f_max, c_max)
            memo[start] = f_max
            return f_max

        ans = 0
        for i in range(n):
            ans = max(ans, recur(i))
        return ans
