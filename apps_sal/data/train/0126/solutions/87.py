import collections


class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counter = collections.defaultdict(int)
        for ln in range(minSize, maxSize + 1):
            for i in range(0, len(s) - ln + 1):
                sub = s[i:i + ln]
                if len(set(sub)) <= maxLetters:
                    counter[sub] += 1
        count = [item[1] for item in counter.items()]
        return max(count) if count else 0
