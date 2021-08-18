class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def permutations(s):
            result = [[s]]
            for i in range(1, len(s)):
                start = [s[:i]]
                end = s[i:]
                for p in permutations(end):
                    result.append(start + p)
            return result

        l = permutations(s)
        maxt = 0
        totalset = set()
        for i in l:
            if len(set(i)) == len(i):
                if len(i) > maxt:
                    maxt = len(i)
        return maxt
