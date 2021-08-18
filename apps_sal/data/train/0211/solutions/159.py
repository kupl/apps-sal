class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def helper(s1_set, s2):
            N = len(s2)
            if N == 1:
                if s2 in s1_set:
                    return 0
                return len(s1_set) + 1
            res = 0 if s2 in s1_set else len(s1_set) + 1
            for i in range(1, N):
                if s2[:i] in s1_set:
                    continue
                s1_set.add(s2[:i])
                res = max(res, helper(s1_set, s2[i:]))
                s1_set.discard(s2[:i])
            return res
        res = helper(set(), s)
        return res
