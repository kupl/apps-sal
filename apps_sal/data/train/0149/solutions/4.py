class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        unique = set(s)
        dups = []

        for c in unique:
            dups.append(c * k)

        while True:
            start = s
            for c in dups:
                s = s.replace(c, '')

            if start == s:
                return s
