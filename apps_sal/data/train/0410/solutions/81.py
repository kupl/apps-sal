class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        pair = []

        def transform(val):

            count = 0

            while val != 1:

                val = val / 2 if val % 2 == 0 else 3 * val + 1
                count += 1

            return count

        for i in range(lo, hi + 1):

            pair.append((transform(i), i))
        print(sorted(pair))
        return sorted(pair)[k - 1][1]
