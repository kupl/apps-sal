class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        res = 1
        if n == 1:
            return res
        for x in range(2**(n - 1)):
            m = 1 << (n - 2)
            p0 = 0
            p1 = 0
            st = set()
            done = False
            while m:
                if x & m:
                    sr = s[p0:p1 + 1]
                    if sr in st:
                        done = True
                        break
                    st.add(sr)
                    p0 = p1 + 1
                    p1 = p1 + 1
                else:
                    p1 += 1
                m >>= 1
            if not done:
                sr = s[p0:p1 + 1]
                if sr not in st:
                    res = max(res, len(st) + 1)
        return res
