class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # dp = [[\"\"] for _ in range(len(s))]
        # dp[0] = [s[0]]
        # for i in range(1, len(s)):
        #     maxnum_ = 1
        #     for j in range(i):
        #         if s[j+1:i] not in dp[j]:
        #             maxnum = len(dp[j]) + 1
        #             if maxnum > maxnum_:
        #                 maxnum_ = maxnum
        #                 dp[i] = dp[j].copy()
        #                 dp[i].append(s[j+1:i])
        # print(dp)
        # return len(dp[len(s)-1])
        #         return len(self.maxUniqueSplit_(s, len(s)-1)[-1])

        #     @lru_cache
        #     def maxUniqueSplit_(self, s, i):
        #         if i == 0:
        #             return [[s[i]]]
        #         else:
        #             max_ = 0
        #             toreturn = []
        #             for j in range(i):
        #                 maxUniqueSplit_j = self.maxUniqueSplit_(s, j)
        #                 for uniquesplit_j in maxUniqueSplit_j:
        #                     if s[j+1:i+1] not in uniquesplit_j:
        #                         if len(uniquesplit_j) + 1 > max_:
        #                             toreturn = [uniquesplit_j + [s[j+1:i+1]]]
        #                             max_ = len(uniquesplit_j) + 1
        #                         elif len(uniquesplit_j) + 1 == max_:
        #                             toreturn.append(uniquesplit_j + [s[j+1:i+1]])
        #                     if j == i - 1 and len(toreturn) == 0:
        #                         toreturn = [uniquesplit_j]
        #             print(toreturn, i)
        #             return toreturn
        if len(s) == 1:
            return 1

        def splitter(str):
            for i in range(1, len(str)):
                start = str[0:i]
                end = str[i:]
                yield (start, end)
                for split in splitter(end):
                    result = [start]
                    result.extend(split)
                    yield result

        maxnum = 0
        for split in splitter(s):
            if len(set(split)) == len(split):
                maxnum = max(len(split), maxnum)
        if maxnum == 0:
            return self.maxUniqueSplit(s[:len(s) - 1])
        else:
            return maxnum
