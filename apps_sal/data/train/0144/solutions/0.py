class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        primeFactors = []
        for i in range(2, int(n**.5) + 1):
            while n % i == 0:
                primeFactors.append(i)
                n = n // i
        if n > 1:
            primeFactors.append(n)
        return sum(primeFactors)
