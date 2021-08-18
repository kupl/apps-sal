class Solution:
    def getProbability(self, balls: List[int]) -> float:
        first, second = [0 for _ in range(len(balls))], [0 for _ in range(len(balls))]

        ret = []
        total = []
        self.good = 0
        self.all = 0
        mem_factorial = {}

        def factorial(v):
            if v not in mem_factorial:
                mem_factorial[v] = v * factorial(v - 1) if v != 0 else 1
            return mem_factorial[v]

        def permutation(arr):
            prod = 1
            for v in arr:
                prod *= factorial(v)
            return factorial(sum(arr)) / prod

        def dfs(i):

            if i == len(balls):
                if sum(first) != sum(second):
                    return
                p1, p2 = permutation(first), permutation(second)
                self.all += p1 * p2
                if sum(v > 0 for v in first) == sum(v > 0 for v in second):
                    self.good += p1 * p2
                return
            for j in range(balls[i] + 1):
                first[i], second[i] = j, balls[i] - j
                dfs(i + 1)
                first[i], second[i] = 0, 0

        dfs(0)
        return self.good / self.all
