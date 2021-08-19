class Solution:

    def numSplitsBF(self, s: str) -> int:
        cntr = 0
        for i in range(1, len(s)):
            (a, b) = (collections.Counter(s[:i]), collections.Counter(s[i:]))
            if len(a) == len(b):
                cntr += 1
        return cntr

    def numSplits(self, s: str) -> int:
        a = collections.defaultdict(int)
        a[s[0]] = 1
        b = collections.Counter(s[1:])
        pntr = 1
        cntr = 0 if len(a) != len(b) else 1
        while pntr < len(s):
            a[s[pntr]] += 1
            b[s[pntr]] -= 1
            if b[s[pntr]] == 0:
                del b[s[pntr]]
            if len(a) == len(b):
                cntr += 1
            pntr += 1
        return cntr
