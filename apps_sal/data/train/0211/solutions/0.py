class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.x, n = 0, len(s)

        def maxUniqueSplit_(i=0, S=set()):
            if s[i:] not in S:
                self.x = max(self.x, len(S) + 1)

            for j in range(i + 1, n):
                if s[i: j] not in S and len(S) + 1 + n - j > self.x:
                    maxUniqueSplit_(j, S.union({s[i: j]}))

        maxUniqueSplit_()
        return self.x
