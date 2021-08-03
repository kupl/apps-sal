class Solution:
    def longestStrChain(self, wordlist: List[str]) -> int:
        wl = set(wordlist)

        def dfs(w):
            # base
            if len(w) == 1:
                return 1
            if w in memo:
                return memo[w]
            # recursive
            l = len(w)
            depth = 0
            for i in range(l):
                next = w[0:i] + w[i + 1:l]  # substring
                if next in wordlist:
                    depth = max(depth, dfs(next))
            memo[w] = depth + 1
            return depth + 1

        memo = {}
        longest = 1
        for word in wordlist:
            longest = max(longest, dfs(word))
        return longest
