class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        l = len(s)
        ans = 0
        for i in range(minSize, maxSize + 1):
            mp = collections.defaultdict(int)
            for j in range(l - i + 1):
                cc = collections.defaultdict(int)
                sub = s[j:j + i]
                if len(set(sub)) <= maxLetters:
                    mp[sub] += 1
            if len(mp.keys()) > 0:
                ans = max(max(mp.values()), ans)
        return ans
