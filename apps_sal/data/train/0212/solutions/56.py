import math


class Solution:

    @staticmethod
    def numFactors(num, A_set):
        factors = set()
        for a in A_set:
            if num % a == 0 and num // a in A_set:
                factors.add(a)
                factors.add(num // a)
        return factors

    @staticmethod
    def numFactoredTrees(root, results, A_set):
        if root in results:
            return results[root]
        factors = Solution.numFactors(root, A_set)
        if len(factors) == 0:
            results[root] = 1
            return 1
        n = 1
        while len(factors) > 0:
            factor = factors.pop()
            remainder = root // factor
            if factor not in results:
                results[factor] = Solution.numFactoredTrees(factor, results, A_set)
            if factor == remainder:
                n += results[factor] * results[factor]
            else:
                factors.remove(remainder)
                if remainder not in results:
                    results[remainder] = Solution.numFactoredTrees(remainder, results, A_set)
                n += results[factor] * results[remainder] * 2
        results[root] = n
        return n

    def numFactoredBinaryTrees(self, A) -> int:
        A_set = set(A)
        results = {}
        return sum([Solution.numFactoredTrees(a, results, A_set) for a in A]) % (10 ** 9 + 7)
