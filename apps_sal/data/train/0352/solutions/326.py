class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        ans = defaultdict(int)
        words.sort(key=len)
        for s in words:
            n = len(s)
            now = 0
            for i in range(n):
                s1, s2 = s[:i], s[i+1:]
                now = max(now, ans[(s1, s2)])
            now += 1
            for i in range(n+1):
                s1, s2 = s[:i], s[i:]
                ans[(s1, s2)] = now
        return max(ans.values())
