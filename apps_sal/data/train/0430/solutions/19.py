class Solution(object):
    def distinctSubseqII(self, S):
        prev = collections.defaultdict(int)
        res = 1
        for c in S:
            new = res - prev[c]
            res += new
            prev[c] += new
        return (res - 1) % (10**9 + 7)  
