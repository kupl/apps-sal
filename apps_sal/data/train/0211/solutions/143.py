class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        N = len(s)

        res = 0
        for mask in itertools.product('10', repeat=N - 1):
            mask = list(mask) + ['1']
            substr = set()
            begin = 0
            i = 0
            valid = True
            while True:
                try:
                    idx = mask.index('1', begin)
                    begin = idx + 1
                    if s[i:idx + 1] in substr:
                        valid = False
                        break
                    substr.add(s[i:idx + 1])
                    i = idx + 1
                except ValueError:
                    break
            if valid:
                res = max(res, mask.count('1'))
        return res
