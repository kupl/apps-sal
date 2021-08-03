class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        sorted(words, key=len, reverse=True)
        depth = [1] * len(words)

        def dfs(word):
            depth = 1
            for i in range(len(word)):
                new_word = word[:i] + word[i + 1:]
                if new_word in words:
                    depth = max(dfs(new_word) + 1, depth)
            seen.append(word)
            return depth

        count = []
        seen = []
        for word in words:
            if word not in seen:
                count.append(dfs(word))
        return max(count)
