class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count = defaultdict(int)
        for size in range(minSize, maxSize + 1):
            for i in range(0, len(s) - size + 1):
                st = s[i:size + i]
                if len(set(st)) <= maxLetters:
                    count[st] += 1
        if len(count) == 0:
            return 0
        return max(count.values())
