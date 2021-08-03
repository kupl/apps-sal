class Solution:
    mod = 10**9 + 7

    def knightDialer(self, N: int) -> int:
        nMap = {
            0: (6, 4),
            1: (6, 8),
            2: (7, 9),
            3: (4, 8),
            4: (3, 9, 0),
            5: (),
            6: (1, 7, 0),
            7: (2, 6),
            8: (1, 3),
            9: (4, 2)
        }

        m = {}  # (position, num)

        def count(start, n):

            if (start, n) in m:
                return m[(start, n)]

            if n == 0:
                return 1

            else:

                num = 0

                for i in nMap[start]:
                    num += count(i, n - 1)

                m[(start, n)] = num

                return num

        ret = 0
        for i in range(10):
            ret = (ret + count(i, N - 1)) % self.mod

        return int(ret)
