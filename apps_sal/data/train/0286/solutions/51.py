# Sep 8, 2020
# Copied from
# https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/discuss/661723/Struggling-with-probability-problems-Read-this./561118
# The idea:
# A permutation is valid if the number of colors in box A is the same as box B.
class Solution:
    def getProbability(self, balls: List[int]) -> float:
        firstHalf, secondHalf = [0 for _ in range(len(balls))], [0 for _ in range(len(balls))]

        valid_permutations = 0
        all_permutations = 0

        # e.g., given v = 3, compute 3! = 3*2*1
        mem_factorial = {}

        def factorial(v):
            if v not in mem_factorial:
                mem_factorial[v] = v * factorial(v - 1) if v != 0 else 1
            return mem_factorial[v]

        # e.g., given arr=[1,1,2,3],compute the number of all distinct permutations, such as `1123`, `1132`..
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

                nonlocal valid_permutations, all_permutations
                all_permutations += p1 * p2
                valid_permutations += p1 * p2 if sum(v > 0 for v in firstHalf) == sum(v > 0 for v in secondHalf) else 0
            else:
                for j in range(balls[i] + 1):
                    firstHalf[i], secondHalf[i] = j, balls[i] - j
                    dfs(i + 1)
                firstHalf[i], secondHalf[i] = 0, 0

        dfs(0)
        return valid_permutations / all_permutations
