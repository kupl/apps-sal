class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        cnt = [[] for i in range(16)]
        min_l = 16
        for i in words:
            min_l = min([min_l, len(i)])
            cnt[len(i) - 1].append(i)

        def match(a, b):
            i = j = 0
            cnt = 0
            while j < len(b):
                if i < len(a) and a[i] == b[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
                    cnt += 1
            return cnt == 1

        def topdown(curr_words):
            if len(curr_words) == 16:
                return 1
            if curr_words in dp:
                return dp[curr_words]

            dp[curr_words] = 1
            for i in cnt[len(curr_words)]:
                if match(curr_words, i):
                    if not i in dp:
                        dp[i] = topdown(i) + 1
                    dp[curr_words] = max([dp[curr_words], dp[i]])
            return dp[curr_words]
        ans = 0
        for i in range(min_l - 1, 16):
            for j in cnt[i]:
                if j in dp:
                    ans = max([ans, dp[j]])
                else:
                    ans = max([ans, topdown(j)])

        return ans
