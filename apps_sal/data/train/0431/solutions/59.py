class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        s = []
        left = [None] * len(A)
        for i in range(len(A)):
            count = 1
            while len(s) > 0 and A[i] <= s[-1][0]:
                count += s.pop()[1]
            s.append((A[i], count))
            left[i] = count
        s = []
        right = [None] * len(A)
        for i in range(len(A) - 1, -1, -1):
            count = 1
            while len(s) > 0 and A[i] < s[-1][0]:
                count += s.pop()[1]
            s.append((A[i], count))
            right[i] = count
        _sum = 0
        for i in range(len(A)):
            _sum = _sum + A[i] * (left[i] * right[i])
        return int(_sum % (1e9 + 7))
