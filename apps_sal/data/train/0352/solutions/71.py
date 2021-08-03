class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        dicti = collections.defaultdict(set)
        for word in words:
            dicti[len(word)].add(word)

        chars = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        memo = {}

        def dist(word):
            if word in memo:
                return memo[word]
            if len(word) + 1 not in dicti:
                memo[word] = 1
                return memo[word]

            n = len(word)
            ans = 0
            for ch in chars:
                for i in range(n + 1):
                    new_word = word[:i] + ch + word[i:]
                    if new_word in dicti[n + 1]:
                        ans = max(ans, dist(new_word))

            memo[word] = ans + 1
            return ans + 1

        ans = 0
        for word in words:
            ans = max(ans, dist(word))
        return ans
