class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        (s1, s2) = ([], [])
        left = [None] * len(A)
        right = [None] * len(A)
        for i in range(len(A)):
            count1 = 1
            while len(s1) > 0 and A[i] <= s1[-1][0]:
                count1 = count1 + s1.pop()[1]
            s1.append((A[i], count1))
            left[i] = count1
            j = len(A) - 1 - i
            count2 = 1
            while len(s2) > 0 and A[j] < s2[-1][0]:
                count2 += s2.pop()[1]
            s2.append((A[j], count2))
            right[j] = count2
        _sum = 0
        for i in range(len(A)):
            _sum = _sum + A[i] * (left[i] * right[i])
        return int(_sum % (1000000000.0 + 7))
