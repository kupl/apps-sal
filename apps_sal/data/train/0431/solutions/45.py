class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(A)
        (left, right) = ([i + 1 for i in range(n)], [n - i for i in range(n)])
        (stackp, stackn) = ([], [])
        for (i, num) in enumerate(A):
            while stackp and num < A[stackp[-1]]:
                stackp.pop()
            left[i] = i - stackp[-1] if stackp else i + 1
            stackp.append(i)
            while stackn and num < A[stackn[-1]]:
                curr = stackn.pop()
                right[curr] = i - curr
            stackn.append(i)
        res = 0
        mod = 10 ** 9 + 7
        for (i, num) in enumerate(A):
            res = (res + left[i] * right[i] * num) % mod
        return res
