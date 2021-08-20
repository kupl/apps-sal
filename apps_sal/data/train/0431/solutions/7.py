class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(A)
        count = [0] * n
        s = []
        for i in range(n):
            while len(s) > 0 and A[i] <= A[s[-1]]:
                s.pop()
            if len(s) == 0:
                count[i] = i + 1
            else:
                count[i] = i - s[-1]
            s.append(i)
        s = []
        for i in range(n - 1, -1, -1):
            while len(s) > 0 and A[i] < A[s[-1]]:
                s.pop()
            if len(s) == 0:
                count[i] *= n - i
            else:
                count[i] *= s[-1] - i
            s.append(i)
        res = 0
        for i in range(n):
            res += count[i] * A[i]
        return res % 1000000007
