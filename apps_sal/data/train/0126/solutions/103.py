class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        currDct = {}
        ansDct = defaultdict(int)
        length = len(s)
        l = 0
        r = 0
        while l + minSize < length + 1:
            currDct = Counter(s[l:l + minSize])
            if len(currDct) <= maxLetters:
                ansDct[s[l:l + minSize]] += 1
            else:
                l += 1
                continue
            if minSize == maxSize:
                l += 1
                continue
            r = l + minSize + 1
            while r < length and r < l + maxSize:
                currDct[s[r]] += 1
                currDct[s[l]] -= 1
                if currDct[s[l]] == 0:
                    del currDct[s[l]]
                if len(currDct) <= maxLetters:
                    ansDct[s[l:r + 1]] += 1
                r += 1
            l += 1
        return 0 if not ansDct else max(ansDct.values())
