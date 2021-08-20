class Solution:

    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        isPrime = [True for _ in range(n + 1)]
        isPrime[1] = False
        prime = []
        for i in range(2, n + 1):
            if isPrime[i] == True:
                prime.append(i)
                k = 1
                while (k + 1) * i <= n:
                    isPrime[(k + 1) * i] = False
                    k += 1
        if isPrime[n]:
            return n
        (cnt, i) = (0, 0)
        while n > 1:
            while n % prime[i] == 0:
                cnt += prime[i]
                n = n // prime[i]
            if isPrime[n]:
                return cnt + n
            i += 1
        return cnt
