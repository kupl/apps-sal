class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        if not s:
            return 0
        splits = [[] for _ in range(len(s))]
        for (i, c) in enumerate(s):
            splits[i].append(set([s[:i + 1]]))
            for j in range(1, i + 1):
                ss = s[j:i + 1]
                for spl in splits[j - 1]:
                    if ss not in spl:
                        splits[i].append(spl | set([ss]))
        return max([len(spl) for spl in splits[-1]])
