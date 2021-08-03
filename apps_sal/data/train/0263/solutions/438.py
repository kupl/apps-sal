class Solution:
    dic = {}
    dic[1] = [6, 8]
    dic[2] = [7, 9]
    dic[3] = [4, 8]
    dic[4] = [0, 3, 9]
    dic[5] = []
    dic[6] = [0, 1, 7]
    dic[7] = [2, 6]
    dic[8] = [1, 3]
    dic[9] = [2, 4]
    dic[0] = [4, 6]

    def knightDialer(self, n: int) -> int:
        mem = defaultdict(int)

        for j in range(10):
            mem[(1, j)] = 1

        for i in range(1, n):
            for j in range(10):
                for num in self.dic[j]:
                    mem[(i + 1, num)] += mem[(i, j)]
                    mem[(i + 1, num)] = mem[(i + 1, num)] % (10**9 + 7)

        res = 0

        for i in range(10):
            res += mem[(n, i)]
            res = res % (10**9 + 7)

        return res
