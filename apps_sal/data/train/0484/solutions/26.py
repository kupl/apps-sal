class Solution:

    def is_prime(self, n):
        small_primes = (2, 3, 5, 7, 11, 13, 17, 19)
        if n == 1:
            return False
        if n in small_primes:
            return True
        for p in small_primes:
            if n % p == 0:
                return False
        check_limit = int(n ** 0.5) + 1
        for p in range(small_primes[-1], check_limit, 2):
            if n % p == 0:
                return False
        return True

    def is_odd_len_palindrome(self, n):
        n_str = str(n)
        total_digit = len(n_str)
        len_is_odd = total_digit % 2 != 0
        if not len_is_odd:
            return False
        half_len_n = int((total_digit + 1) / 2)
        if n_str[:half_len_n] != n_str[total_digit - half_len_n:][::-1]:
            return False
        return True

    def find_odd_len_palindrome_after_n(self, n):
        if n < 9:
            return n + 1
        elif n < 11:
            return 11
        n_str = str(n)
        total_digit = len(n_str)
        len_is_odd = total_digit % 2 != 0
        if not len_is_odd:
            return int('1' + '0' * (total_digit - 1) + '1')
        half_len_n = int((total_digit + 1) / 2)
        left_str = n_str[:half_len_n]
        right_str = left_str[:total_digit - half_len_n][::-1]
        p = int(left_str + right_str)
        if p > n:
            return p
        else:
            left = int(left_str)
            left += 1
            increase_digit = len(str(left)) > len(left_str)
            left_str = str(left)
            if increase_digit:
                return int('1' + '0' * total_digit + '1')
            left_str = left_str[:half_len_n]
            right_str = left_str[:total_digit - half_len_n][::-1]
            return int(left_str + right_str)

    def primePalindrome(self, N: int) -> int:
        if self.is_odd_len_palindrome(N) and self.is_prime(N):
            return N
        elif N == 11:
            return N
        i = self.find_odd_len_palindrome_after_n(N)
        while i < 2 * 10 ** 8:
            if self.is_prime(i):
                return i
            i = self.find_odd_len_palindrome_after_n(i)
        return i
