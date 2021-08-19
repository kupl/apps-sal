class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        table = defaultdict(list)
        for w in words:
            table[len(w)].append(w)
        max_len = max((len(w) for w in words))

        def backtracking(cur, n):
            if len(cur) == max_len:
                return 0
            if not cur in dp:
                res = 0
                for word in table[n]:
                    for i in range(len(word)):
                        if word[0:i] + word[i + 1:] == cur:
                            res = max(res, backtracking(word, n + 1) + 1)
                            break
                dp[cur] = res
            return dp[cur]
        res = 0
        for (i, v) in table.items():
            for w in v:
                res = max(res, backtracking(w, i + 1) + 1)
        return res
