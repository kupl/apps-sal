class Solution:

    def splitArraySameAverage(self, A: List[int]) -> bool:
        tot = sum(A)
        n = len(A)
        target = tot / n
        visited = [False] * len(A)
        m = n // 2
        possible = False
        for i in range(1, m + 1):
            if tot * i % n == 0:
                possible = True
                break
        if not possible:
            return False
        A.sort()

        def helper(A, cursum, curcnt, pos):
            if curcnt == 0:
                return cursum == 0
            for i in range(pos, len(A) - curcnt + 1):
                if i > pos and A[i] == A[i - 1]:
                    continue
                if helper(A, cursum - A[i], curcnt - 1, i + 1):
                    return True
            return False
        for i in range(1, m + 1):
            if tot * i % n == 0 and helper(A, tot * i / n, i, 0):
                return True
        return False
