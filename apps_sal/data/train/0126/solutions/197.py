class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        subcount = defaultdict(int)

        for i in range(len(s) - minSize + 1):
            sub = s[i:i + minSize]
            if len(set(sub)) <= maxLetters:
                subcount[sub] += 1

        x = sorted(subcount.values(), reverse=True)
        if not x:
            return 0
        return x[0]
