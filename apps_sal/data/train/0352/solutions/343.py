class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        sets = collections.defaultdict(set)
        (n, dp) = (0, {})
        for word in words:
            n = max(n, len(word))
            sets[len(word)].add(word)
            dp[word] = 1
        ans = 1
        for i in reversed(list(range(2, n + 1))):
            if i - 1 not in sets:
                continue
            for word in sets[i]:
                for j in range(len(word)):
                    new_word = word[:j] + word[j + 1:]
                    if new_word in sets[i - 1]:
                        dp[new_word] = dp[word] + 1
                        ans = max(ans, dp[new_word])
        return ans
