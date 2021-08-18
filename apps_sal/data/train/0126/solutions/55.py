class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        mymap = collections.defaultdict(int)
        st, j, n = 0, 0, len(s)
        while st + minSize <= n:
            count = collections.Counter(s[st:st + minSize - 1])
            for j in range(st + minSize - 1, st + maxSize):
                if j >= n:
                    break
                count[s[j]] += 1
                if len(count) <= maxLetters:
                    mymap[s[st:j + 1]] += 1
            st += 1
        maxval = max(list(mymap.values()) or [0])
        return maxval
