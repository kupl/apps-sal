class Solution:

    def knightDialer(self, N: int) -> int:
        mod = 10 ** 9 + 7

        def getNeighbors(N):
            neighs = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
            return neighs[N]

        def getCount(start, n):
            if (start, n) not in dic:
                if n == 0:
                    dic[start, n] = 1
                else:
                    count = 0
                    for nei in getNeighbors(start):
                        count += getCount(nei, n - 1)
                    dic[start, n] = count
            return dic[start, n]
        dic = {}
        val = 0
        for i in range(10):
            val += getCount(i, N - 1)
        return val % mod
