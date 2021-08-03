class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = [x for x in range(1, n + 1)]

        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i - 1] * (i)

        result = []

        for i in range(1, n + 1):
            index = (k - 1) // factorial[n - i]
            k = k % factorial[n - i]

            result.append(numbers[index])
            numbers.remove(numbers[index])
        return ''.join(map(str, result))
