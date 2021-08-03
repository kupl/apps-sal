class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        d = defaultdict(int)
        s = list(s)
        n = len(s)

        for i in range(n - minSize + 1):
            for j in range(i + minSize, min(i + maxSize + 1, n + 1)):
                if len(set(s[i:j])) <= maxLetters:
                    d[tuple(s[i:j])] += 1

                else:
                    break
        if not d:
            return 0
        return max(d.values())
