class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # sliding window, subtract left, if == 0, delete from dict (sliding caterpillar)
        currDct = {}
        ansDct = defaultdict(int)
        length = len(s)
        l = 0; r = 0
        # init to min size; caterpillar sliding window
        while l + minSize < length+1:
            # expand to min
            currDct = Counter(s[l:l+minSize])
            if len(currDct) <= maxLetters:
                ansDct[s[l:l+minSize]] += 1
            else: l += 1; continue
            # expand to maxSize
            if minSize == maxSize: l += 1; continue
            r = l + minSize + 1;
            while r < length and r < l + maxSize:
                # add to the right
                currDct[s[r]] += 1
                # del to the left
                currDct[s[l]] -= 1
                if currDct[s[l]] == 0: del currDct[s[l]]
                if len(currDct) <= maxLetters:
                    ansDct[s[l:r+1]] += 1
                r += 1
            l += 1
        # print(ansDct)
        return 0 if not ansDct else max(ansDct.values())
