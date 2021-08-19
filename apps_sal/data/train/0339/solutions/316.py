class Solution:

    def numTriplets(self, A: List[int], B: List[int]) -> int:

        def find(X, Y):
            res = 0
            for x in X:
                have = collections.Counter(Y)
                for (i, y) in enumerate(Y):
                    have[y] -= 1
                    if x * x % y == 0:
                        res += have[x * x // y]
            return res
        return find(A, B) + find(B, A)
