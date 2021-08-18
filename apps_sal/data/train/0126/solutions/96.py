class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        cnt = Counter()
        for size in range(minSize, maxSize + 1):
            for i in range(len(s) - size + 1):
                ss = s[i:i + size]
                if len(set(ss)) <= maxLetters:
                    cnt[ss] += 1
        return max(cnt.values()) if cnt else 0
