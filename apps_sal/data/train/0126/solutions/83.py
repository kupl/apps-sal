class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        results = 0
        for l in range(minSize, maxSize + 1):
            if l <= n:
                maps = {}
                for i in range(n - l + 1):
                    subs = s[i:i + l]
                    if len(set(subs)) <= maxLetters:
                        try:
                            maps[subs] += 1
                            if maps[subs] > results:
                                results = maps[subs]
                        except KeyError:
                            maps[subs] = 1
                            if maps[subs] > results:
                                results = maps[subs]
        return results
