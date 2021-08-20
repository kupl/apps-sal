class Solution:

    def numTriplets(self, a: List[int], b: List[int]) -> int:

        def count(a, b):
            ret = 0
            for x in a:
                c = Counter()
                for y in b:
                    square = x * x
                    if square % y == 0:
                        ret += c[square // y]
                    c[y] += 1
            return ret
        return count(a, b) + count(b, a)
