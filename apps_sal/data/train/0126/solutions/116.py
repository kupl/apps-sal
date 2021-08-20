class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        if len(s) < minSize:
            return 0
        res = 0

        def is_good(ss):
            return len(set(ss)) <= maxLetters
        for sz in range(minSize, maxSize + 1):
            cnt = collections.defaultdict(int)
            for i in range(len(s) - sz + 1):
                if is_good(s[i:i + sz]):
                    cnt[s[i:i + sz]] += 1
                    res = max(res, cnt[s[i:i + sz]])
        return res
