class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        import sys
        from functools import lru_cache

        @lru_cache(None)
        def knapsack(i, num, tot):
            # Find num items in A that add up to tot
            if i > len(A) - 1 or num <= 0 or tot <= 0:
                return False
            elif num == 1 and A[i] == tot:
                return True
            else:
                include = knapsack(i + 1, num - 1, tot - A[i])
                exclude = knapsack(i + 1, num, tot)

                if include:
                    return True
                elif exclude:
                    return True
            return None
        sys.setrecursionlimit(100000)
        tot = sum(A)
        n = len(A)

        gcd = math.gcd(tot, n)

        num = n // gcd
        A = sorted(A)

        for i in range(1, n):
            if (tot * i) % n == 0:
                k = knapsack(0, i, tot * i // n)
                if k is not None:
                    return True
        return False
