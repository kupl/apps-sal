class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(A)
        left = [0] * n
        right = [0] * n
        s = []
        
        for i in range(n):
            count = 1
            while s and s[-1][0] >= A[i]:
                count += s.pop()[1]
            left[i] = count
            s.append((A[i], count))
        s = []
        for i in range(n-1, -1, -1):
            count = 1
            while s and s[-1][0] > A[i]:
                count += s.pop()[1]
            right[i] = count
            s.append((A[i], count))
        print(left)
        print(right)
        s = 0
        for i in range(n):
            s += (left[i]) * (right[i]) * A[i]
        return s % (10 **9 + 7)
