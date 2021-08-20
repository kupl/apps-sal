class Solution:

    def uniqueLetterString(self, s: str) -> int:
        result = 0
        mat = collections.defaultdict(list)
        for (i, ch) in enumerate(s):
            if mat[ch]:
                mat[ch].append(i)
            else:
                mat[ch] = [i]

        def helperF(ranges, n):
            res = 0
            i = 0
            while i < len(ranges):
                elem = ranges[i]
                lef = None
                right = None
                if i > 0:
                    left = ranges[i] - ranges[i - 1]
                else:
                    left = ranges[i] + 1
                if i != len(ranges) - 1:
                    right = ranges[i + 1] - ranges[i]
                else:
                    right = n - ranges[i]
                res += left * right
                i += 1
            return res
        for ch in mat:
            result += helperF(mat[ch], len(s))
        return result
