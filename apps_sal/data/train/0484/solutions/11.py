class Solution:

    def primePalindrome(self, N: int) -> int:
        digits = len(str(N))
        while True:
            for num in self.get_pali(digits):
                if num >= N and self.is_prime(num):
                    return num
            digits += 1

    def get_pali(self, digits):
        if digits == 0:
            yield 0
        elif digits == 1:
            for i in range(10):
                yield i
        elif digits % 2 == 0:
            half = digits // 2
            for i in range(10 ** (half - 1), 10 ** half):
                yield int(str(i) + str(i)[::-1])
        else:
            half = digits // 2
            for i in range(10 ** (half - 1), 10 ** half):
                for j in range(10):
                    yield int(str(i) + str(j) + str(i)[::-1])

    def is_prime(self, num):
        if num < 2:
            return False
        if num == 2:
            return True
        for i in range(2, int(num ** 0.5 + 1)):
            if num % i == 0:
                return False
        return True
