import operator


class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq = collections.defaultdict(int)
        for size in range(minSize, maxSize + 1):
            j = size
            window = s[0:size]
            while j <= len(s):
                if len(set(window)) <= maxLetters:
                    freq[window] += 1
                j += 1
                window = s[j - size:j]
        if freq:
            return max(freq.items(), key=operator.itemgetter(1))[1]
        else:
            return 0
