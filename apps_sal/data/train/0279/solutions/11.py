class Solution:

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        string = ''
        selection = [i for i in range(n + 1)]
        while n > 0:
            (quo, temp) = divmod(k - 1, self.factorial(n - 1))
            string += str(selection[quo + 1])
            selection.remove(selection[quo + 1])
            n -= 1
            k = temp + 1
        return string

    def factorial(self, n):
        if not n:
            return 1
        product = 1
        for i in range(1, n + 1):
            product *= i
        return product
