class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        a = [float('-inf')] + arr + [float('inf')]
        n = len(a)
        nondecrleft = [0] * n
        nondecrleft[0] = 1
        for i in range(1, n):
            if a[i] < a[i - 1]:
                break
            nondecrleft[i] = 1

        nondecrright = [0] * n
        nondecrright[n - 1] = 1
        for i in range(n - 2, -1, -1):
            if a[i] > a[i + 1]:
                break
            nondecrright[i] = 1

        def f(l):
            for i in range(1, n - l):
                if nondecrleft[i - 1] and nondecrright[i + l] and a[i - 1] <= a[i + l]:
                    return True
            return False
        lo, hi = 0, n - 2
        while lo != hi:
            p = (lo + hi) // 2
            if not f(p):
                lo = p + 1
            else:
                hi = p
        return lo
