class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0
        words.sort(key=len)
        dp = [1 for _ in range(len(words))]
        start = collections.defaultdict(int)
        end = collections.defaultdict(int)
        for i in range(len(words) - 1, -1, -1):
            start[len(words[i])] = i
        if len(start) == 1:
            return 1
        for i in range(len(words)):
            end[len(words[i])] = i
        res = 1
        for i in range(start[len(words[0]) + 1], len(words)):
            for j in range(start[len(words[i]) - 1], end[len(words[i]) - 1] + 1):
                charA = set(words[j])
                charB = set(words[i])
                intersect = len(charA.intersection(charB))
                if intersect == len(charA):
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res
