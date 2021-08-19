from collections import defaultdict


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        memo = [[] for _ in range(n)]

        def unique_split(i):
            if memo[i]:
                return memo[i]
            memo[i].append(set([s[:i + 1]]))
            for j in range(i):
                sets = unique_split(j)
                for sub in sets:
                    if s[j + 1:i + 1] not in sub:
                        memo[i].append(sub | set([s[j + 1:i + 1]]))
            return memo[i]
        sublen = [len(lst) for lst in unique_split(n - 1)]
        # print(memo)
        return max(sublen)
