class Solution:
    def helper(self, memo, s, w):
        if w in memo:
            return memo[w]
        count = 0
        for i in range(len(w)):
            pre = w[:i] + w[i + 1:]
            if pre in s:
                count = max(count, self.helper(memo, s, pre))
        memo[w] = 1 + count
        return 1 + count

    def longestStrChain(self, words: List[str]) -> int:
        ans = 0
        memo = {}
        for w in words:
            ans = max(ans, self.helper(memo, set(words), w))
        return ans
