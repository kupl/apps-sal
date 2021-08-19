class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        dp = [1 for _ in range(len(words) + 1)]
        dp[0] = 0
        words = sorted(words, key=lambda x: len(x))
        hmap = collections.defaultdict(list)
        for (i, word) in enumerate(words):
            hmap[len(word)] += [(word, i)]
        for i in range(1, len(words) + 1):
            key = len(words[i - 1]) - 1
            for (word, idx) in hmap[key]:
                if self.predecessor(word, words[i - 1]):
                    dp[i] = max(dp[i], dp[idx + 1] + 1)
        return max(dp)

    def predecessor(self, word0, word1):
        cnt0 = collections.Counter(word0)
        cnt1 = collections.Counter(word1)
        for key in cnt0:
            if key not in cnt1:
                return False
        return True
