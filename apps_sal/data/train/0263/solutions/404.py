class Solution:
    arr = None

    def knightDialer(self, n: int) -> int:
        self.init_arr(n)
        if n == 1:
            return 10
        total = 0
        for j in range(2, n + 1):
            for i in range(10):
                self.dialStart(i, j)
        return self.get_ans(n)

    def get_ans(self, n):
        total = 0
        for i in range(10):
            total = (total + self.arr[i][n]) % 1000000007
        return total

    def init_arr(self, n):
        self.arr = [[0] * (n + 1) for i in range(10)]
        for i in range(10):
            self.arr[i][1] = 1

    def dialStart(self, start: int, n: int):
        neighbours = self.get_neighbours()
        total = 0
        for ne in neighbours[start]:
            total = (total + self.arr[ne][n - 1]) % 1000000007
        self.arr[start][n] = total

    def get_neighbours(self):
        return {0: [4, 6], 1: [8, 6], 2: [7, 9], 3: [8, 4], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
