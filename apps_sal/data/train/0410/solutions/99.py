class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def transform(x):
            steps = 0
            while x != 1:
                if x & 1 == 0:
                    x //= 2
                else:
                    x = (3 * x) + 1
                steps += 1

            return steps

        arr = list(range(lo, hi + 1))
        arr.sort(key=lambda x: (transform(x), x))

        return arr[k - 1]
