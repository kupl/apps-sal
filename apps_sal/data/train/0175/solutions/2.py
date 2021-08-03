class Solution:
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        A = bin(num)[2:][::-1]

        a = [0 for _ in range(len(A))]

        b = [0 for _ in range(len(A))]

        a[0] = 1
        b[0] = 1

        for i in range(1, len(A)):
            a[i] = a[i - 1] + b[i - 1]
            b[i] = a[i - 1]

        n = len(A)
        res = a[n - 1] + b[n - 1]
        for i in range(n - 2, -1, -1):
            if A[i] == '1' and A[i + 1] == '1':
                break
            elif A[i] == '0' and A[i + 1] == '0':
                res -= b[i]
        return res
