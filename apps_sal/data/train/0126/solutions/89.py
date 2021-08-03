class Solution:
    def maxFreq(self, s: str, maxLetters: int, a: int, b: int) -> int:
        cnt = collections.defaultdict(int)
        for i in range(len(s) - a + 1):
            cnt[s[i:i + a]] += 1
        for a, v in sorted(cnt.items(), key=lambda x: x[1], reverse=True):
            if len(set(a)) <= maxLetters:
                return v
        return 0
