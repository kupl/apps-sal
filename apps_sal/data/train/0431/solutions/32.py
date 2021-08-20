class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        (n, mod) = (len(A), 10 ** 9 + 7)
        s = []
        left = [i + 1 for i in range(n)]
        right = [n - i for i in range(n)]
        res = 0
        for i in range(n):
            while s and A[s[-1]] > A[i]:
                k = s.pop()
                right[k] = i - k
            left[i] = i + 1 if not s else i - s[-1]
            s.append(i)
        print(right)
        print(left)
        return sum((a * i * j for (a, i, j) in zip(A, left, right))) % mod
