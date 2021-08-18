class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        result = 1
        for l in itertools.product([True, False], repeat=len(s)):
            if l[-1] == False:
                continue
            cache = list()
            now = ''
            for c, end in zip(s, l):
                now += c
                if end:
                    cache.append(now)
                    now = ''
            if len(cache) == len(set(cache)):
                result = max(result, len(cache))
        return result
