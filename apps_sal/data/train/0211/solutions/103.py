class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        res = [[s[0]]]
        for i in s[1:]:
            for _ in range(len(res)):
                j = res.pop(0)
                res.append(j + [i])
                res.append(j[:-1] + [j[-1] + i])
        return max(list(map(len, list(map(set, res)))))
