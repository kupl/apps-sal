class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0
        dp = [1 for _ in words]
        largest = 1
        words.sort(key=lambda s:len(s))
        print(words)
        def predecessor(big_word, small_word):
            b = 0
            s = 0
            mismatch = False
            if len(small_word) + 1 != len(big_word):
                return False
            while b < len(big_word) and s < len(small_word):
                if big_word[b] != small_word[s] and not mismatch:
                    mismatch = True
                    b += 1
                    continue
                elif big_word[b] == small_word[s]:
                    s += 1
                    b += 1
                    continue
                else:
                    return False
            return True

        left = 0
        right = 0
        while right < len(words):
            for k in range(left, right):
                if len(words[k]) == words[right]:
                    left = right
                    break
                if predecessor(words[right], words[k]):
                    dp[right] = max(dp[right], dp[k] + 1)
                    largest = max(dp[right], largest)
            right += 1
        return largest
