import math


class Solution:
    def getProbability(self, balls):
        k = len(balls)
        first = [0 for _ in range(k)]
        second = [0 for _ in range(k)]

        factorial_memo = {}
        valid = 0
        successful = 0

        def getFactorial(v):
            if v not in factorial_memo:
                factorial_memo[v] = math.factorial(v)

            return factorial_memo[v]

        def getPermutation(lst):
            sum1 = 0
            for i in lst:
                sum1 += getFactorial(i)
            return getFactorial(sum(lst)) / sum1

        def dfs(i):

            if i == k:
                if sum(first) != sum(second):
                    return
                valid += getPermutation(first) * getPermutation(second)
                if sum([v > 0 for v in getPermutation(first)]) == sum([v > 0 for v in getPermutation(second)]):
                    successful += getPermutation(first) * getPermutation(second)
            else:
                for n in range(balls[i] + 1):
                    first[i] = n
                    second[i] = balls[i] - n
                    dfs(i + 1)

        dfs(0)
        return successful / valid

    def getProbability(self, balls: List[int]) -> float:
        firstHalf, secondHalf = [0 for _ in range(len(balls))], [0 for _ in range(len(balls))]
        self.good, self.all = 0, 0

        mem_factorial = {}

        def factorial(v):
            if v not in mem_factorial:
                mem_factorial[v] = math.factorial(v)
            return mem_factorial[v]

        def permutation(arr):
            prod = 1
            for v in arr:
                prod *= factorial(v)
            return factorial(sum(arr)) / prod

        def dfs(i):
            if i == len(balls):
                if sum(firstHalf) != sum(secondHalf):
                    return
                p1, p2 = permutation(firstHalf), permutation(secondHalf)
                self.all += p1 * p2
                self.good += p1 * p2 if sum(v > 0 for v in firstHalf) == sum(v > 0 for v in secondHalf) else 0
            else:
                for j in range(balls[i] + 1):
                    firstHalf[i], secondHalf[i] = j, balls[i] - j
                    dfs(i + 1)
                    firstHalf[i], secondHalf[i] = 0, 0
        dfs(0)
        return self.good / self.all
