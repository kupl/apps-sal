class Solution:

    def numTriplets(self, a: List[int], b: List[int]) -> int:

        def count(a, b):
            c = Counter()
            for (x, y) in combinations(b, 2):
                c[x * y] += 1
            ret = 0
            for x in a:
                ret += c[x * x]
            return ret
        return count(a, b) + count(b, a)
