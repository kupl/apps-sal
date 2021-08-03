class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq = collections.defaultdict(int)

        for i in range(len(s) - minSize + 1):
            freq[s[i:i + minSize]] += 1

        mx = 0

        for key in freq:
            if len(set(key)) <= maxLetters and mx < freq[key]:
                mx = freq[key]

        return mx
