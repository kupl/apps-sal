class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        x = defaultdict(int)
        for i in range(len(s) - minSize + 1):
            sub = s[i:i + minSize]
            if len(set(sub)) <= maxLetters:
                x[sub] += 1
        return max(x.values(), default=0)
