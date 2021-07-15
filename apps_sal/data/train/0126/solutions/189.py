class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        ans = 0
        l = minSize
        counts = {}
        for i in range(len(s) - l + 1):
            string = s[i:i+l]
            c = collections.Counter(string)
            if len(c) <= maxLetters:
                counts[string] = counts.get(string, 0) + 1

        if counts:
            ans = max(ans, max(counts.values()))
        
        return ans
