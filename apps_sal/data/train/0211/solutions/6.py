class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        if not s:
            return 0
        splits = [[] for _ in range(len(s))]
        best_len = 0
        for i, c in enumerate(s):
            splits[i].append(set([s[:i + 1]]))
            best_len = max(best_len, 1)
            for j in range(1, i + 1):
                ss = s[j: i + 1]
                for spl in splits[j - 1]:
                    if ss not in spl:
                        best_len = max(best_len, len(spl) + 1)
                        splits[i].append(spl | set([ss]))
        return best_len
