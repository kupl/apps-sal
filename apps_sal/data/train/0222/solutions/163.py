class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        A_set = set(A)
        res_set = []
        res = 0
        for i in range(n - 2):
            for j in range(i + 1, n):
                if A[i] + A[j] in A_set:
                    res_set.append((A[j], A[i] + A[j]))
        if res_set:
            res = 3
        else:
            return 0
        while res_set:
            length = len(res_set)
            while length:
                (x, y) = res_set.pop(0)
                if x + y in A_set:
                    res_set.append((y, x + y))
                length -= 1
            if res_set:
                res += 1
        return res
