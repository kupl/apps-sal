class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dict = defaultdict()

        def weight(x):
            if(x == 1):
                return 1
            if(x % 2 == 0):
                return 1 + weight(x // 2)
            else:
                return 1 + weight(3 * x + 1)

        for i in range(lo, hi + 1):
            dict[i] = weight(i)

        dict = sorted(list(dict.items()), key=lambda x: x[1])
        return dict[k - 1][0]
