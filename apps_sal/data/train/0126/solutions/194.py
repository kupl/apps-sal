class Solution:
    from collections import Counter
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        c = 0
        freq = collections.defaultdict(int)
        for i in range(len(s)-minSize+1):
            p = s[i:i+minSize]
            cur_dict = Counter(p)
            if len(cur_dict) <= maxLetters:
                freq[p] += 1
        if freq:
            return max(freq.values())
        return 0

