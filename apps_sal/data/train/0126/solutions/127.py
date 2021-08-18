class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        cnt = Counter()
        for sz in range(minSize, min(maxSize, len(s)) + 1):
            cur = Counter(s[:sz])
            if len(cur) <= maxLetters:
                cnt[s[:sz]] += 1
            for i in range(1, len(s) - sz + 1):
                cur[s[i + sz - 1]] += 1
                cur[s[i - 1]] -= 1
                if cur[s[i - 1]] == 0:
                    cur.pop(s[i - 1])
                if len(cur) <= maxLetters:
                    cnt[s[i:i + sz]] += 1
        return max(cnt.values()) if cnt else 0
