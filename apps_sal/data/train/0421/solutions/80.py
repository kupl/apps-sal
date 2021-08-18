class Solution:
    def lastSubstring(self, s: str) -> str:
        if not s:
            return None
        maxC, N = max(s), len(s)
        inds = [i for i in range(N) if s[i] == maxC and (i == 0 or s[i - 1] != maxC)]
        maxind = inds[0]

        for i in range(1, len(inds)):
            curind = inds[i]
            if self.compare(s[curind:], s[maxind:]):
                maxind = curind

        return s[maxind:]

    def compare(self, s1, s2):
        i = 0
        while i < len(s1):
            if s1[i] > s2[i]:
                return True
            elif s1[i] < s2[i]:
                return False
            i += 1
        return False
