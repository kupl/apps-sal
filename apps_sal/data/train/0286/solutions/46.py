import math


class Solution:
    def getProbability(self, balls):
        k = len(balls)
        first = [0 for _ in range(k)]
        second = [0 for _ in range(k)]

        factorial_memo = {}
        self.valid = 0
        self.successful = 0

        def getFactorial(v):
            if v not in factorial_memo:
                factorial_memo[v] = math.factorial(v)

            return factorial_memo[v]

        def getPermutation(lst):
            prod = 1
            for i in lst:
                prod *= getFactorial(i)
            return getFactorial(sum(lst)) / prod

        def dfs(i):

            if i == k:
                if sum(first) != sum(second):
                    return
                self.valid += getPermutation(first) * getPermutation(second)
                if sum([v > 0 for v in first]) == sum([v > 0 for v in second]):
                    self.successful += getPermutation(first) * getPermutation(second)
            else:
                for n in range(balls[i] + 1):
                    first[i] = n
                    second[i] = balls[i] - n
                    dfs(i + 1)
        dfs(0)
        return self.successful / self.valid
