class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        s1, s2 = [], []
        left = [None] * len(A)
        right = [None] * len(A)

        for i in range(len(A)):
            count = 1
            while len(s1) > 0 and A[i] <= s1[-1][0]:
                count += s1.pop()[1]
            s1.append((A[i], count))
            left[i] = count

        for i in range(len(A) - 1, -1, -1):
            count = 1
            while len(s2) > 0 and A[i] < s2[-1][0]:
                count += s2.pop()[1]
            s2.append((A[i], count))
            right[i] = count
        _sum = 0
        for i in range(len(A)):
            _sum = _sum + A[i] * (left[i] * right[i])
        return int(_sum % (1e9 + 7))
