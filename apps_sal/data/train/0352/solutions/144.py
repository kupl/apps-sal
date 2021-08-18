class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        def is_predecessor(word_short, word_long) -> bool:
            if len(word_short) + 1 != len(word_long):
                return False
            i_s = 0
            can_skip = True
            for i_l in range(len(word_long)):
                if i_s > len(word_short) - 1:
                    return True
                c_s = word_short[i_s]
                c_l = word_long[i_l]
                if c_s == c_l:
                    i_s += 1
                else:
                    if can_skip:
                        can_skip = False
                        pass
                    else:
                        return False
            return True

        if not words:
            return 0

        words.sort(key=lambda x: len(x))
        dp = [1] * len(words)

        for r in range(1, len(words)):
            for l in range(r):
                if is_predecessor(words[l], words[r]):
                    dp[r] = max(dp[r], dp[l] + 1)

        return max(dp)
