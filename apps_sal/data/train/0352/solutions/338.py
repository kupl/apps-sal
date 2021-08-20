class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        by_length = collections.defaultdict(set)
        for w in words:
            by_length[len(w)].add(w)
        for (i, l) in enumerate(sorted(by_length.keys())):
            if i == 0:
                for w in by_length[l]:
                    dp[w] = 1
            elif not by_length[l - 1]:
                for w in by_length[l]:
                    dp[w] = 1
            else:
                for w in by_length[l]:
                    dp[w] = 1
                    for j in range(len(w)):
                        candidate = w[:j] + w[j + 1:]
                        if candidate in by_length[l - 1]:
                            dp[w] = max(dp[w], dp[candidate] + 1)
        return max(dp.values())
