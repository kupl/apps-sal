class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq = collections.defaultdict(int)
        max_freq = 0
        for win in range(minSize, maxSize + 1):
            for i in range(len(s) - win + 1):
                sub_seq = s[i:i + win]
                if len(set(sub_seq)) <= maxLetters:
                    freq[sub_seq] += 1
            max_freq = max(max_freq, max(freq.values()) if freq else 0)
        return max_freq
