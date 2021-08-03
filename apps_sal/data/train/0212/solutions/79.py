class Solution:
    def numFactoredBinaryTrees(self, A):

        t = {}
        for a in sorted(A):
            t[a] = 1 + sum(t[b] * t.get(a / b, 0) for b in A if b < a)
        return sum(t.values()) % (10**9 + 7)
