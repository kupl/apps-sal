class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        d = dict()
        n = len(s)
        for i in range(n):
            j = i
            st = set()
            l = 0
            while j < min(n, i + maxSize) and l <= maxLetters:
                if s[j] not in st:
                    l += 1
                    st.add(s[j])
                x = s[i:j + 1]
                ln = j - i + 1
                if ln >= minSize and ln <= maxSize and l <= maxLetters:
                    if x in d:
                        d[x] += 1
                    else:
                        d[x] = 1
                j += 1
        if d == dict():
            return 0
        return max(list(d.values()))
