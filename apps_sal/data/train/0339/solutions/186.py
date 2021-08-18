class Solution:
    def numTriplets(self, A: List[int], B: List[int]) -> int:
        res = 0

        def count(n2, arr):
            res = 0
            c = defaultdict(int)
            for n in arr:
                if n2 % n == 0:
                    res += c[n2 // n]
                c[n] += 1
            return res

        for i, n in enumerate(A):
            res += count(n * n, B)
        for i, n in enumerate(B):
            res += count(n * n, A)
        return res
