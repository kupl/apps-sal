class Solution:

    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A.sort()
        t = {}
        for a in A:
            t[a] = 1 + sum((t[b] * t.get(a / b, 0) for b in A if b < a))
        return sum(t.values()) % (pow(10, 9) + 7)
