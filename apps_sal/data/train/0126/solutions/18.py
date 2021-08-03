class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        c = Counter()
        i = 0
        letterlen = 0
        maxSize = maxSize + 1 if maxSize == minSize else maxSize
        ans = Counter()
        for j, v in enumerate(s):
            c[v] += 1
            if c[v] == 1:
                letterlen += 1
            while letterlen > maxLetters:
                x = s[i]
                c[x] -= 1
                if c[x] == 0:
                    letterlen -= 1
                i += 1
            # print(i,j)
            for l in range(minSize, maxSize):
                beg = j - l + 1
                # print(i,j,beg)
                if beg >= i:
                    ans[s[beg:j + 1]] += 1
        # print(ans)
        return max(ans.values()) if ans else 0
