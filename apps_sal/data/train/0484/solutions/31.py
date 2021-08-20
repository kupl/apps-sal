class Solution:

    def primePalindrome(self, N: int) -> int:

        def isPrime(x):
            """
            for i in range(2,int(sqrt(x))+1):
                if x % i == 0:
                    return False
            return True
            """
            return x > 1 and all((x % d for d in range(2, int(x ** 0.5) + 1)))

        def isPalindrome(x):
            x = str(x)
            if len(x) == 1:
                return True
            i = 0
            j = len(x) - 1
            while i < j:
                if x[i] == x[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True
        if N <= 1:
            return 2
        i = N
        while True:
            if str(i) == str(i)[::-1] and isPrime(i):
                return i
            i += 1
            if 10 ** 7 < i < 10 ** 8:
                i = 10 ** 8
        return -1
