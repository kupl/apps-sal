class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        seen = Counter()
        cnt = Counter()
        j = 0
        for i, ss in enumerate(s):
            cnt[ss] += 1
            while len(cnt) > maxLetters and j <= i:
                cnt[s[j]] -= 1
                if not cnt[s[j]]:
                    del cnt[s[j]]
                j += 1
            k = j
            while i - k + 1 >= minSize:
                if i - k + 1 <= maxSize:
                    seen[s[k: i + 1]] += 1
                k += 1
        return max(seen.values()) if seen else 0
