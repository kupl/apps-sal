class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def check(st, cm):
            mx = 0 if st in cm else 1
            for i in range(1, len(st)):
                a = st[:i]
                b = st[i:]
                if a not in cm:
                    ncm = set(cm)
                    ncm.add(a)
                    c = check(b, ncm) + 1
                    if c > mx:
                        mx = c
            return mx

        return check(s, set())
