class Solution:
    def primePalindrome(self, N: int) -> int:

        def get_palindromes(n):
            if n == 1:
                for i in range(10):
                    yield i
            elif n % 2 == 0:
                d = n // 2
                for i in range(10**(d - 1), 10**d):
                    s = str(i)
                    yield int(s + s[::-1])
            else:
                d = n // 2
                for i in range(10**(d - 1), 10**d):
                    s = str(i)
                    for j in range(10):
                        yield int(s + str(j) + s[::-1])

        def check_prime(num):
            if num == 1:
                return False
            elif num == 2:
                return True
            for i in range(2, int(num**0.5 + 1)):
                if num % i == 0:
                    return False
            return True

        digits = len(str(N))
        while True:
            for n in get_palindromes(digits):
                if n >= N and check_prime(n):
                    return n
            digits += 1
