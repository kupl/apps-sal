class Solution:

    def is_prime(n: int) -> bool:
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i = i + 1
        return True

    def is_palindrome(n: int) -> bool:
        num_string = str(n)
        num_length = len(num_string)
        if num_string[num_length - 1] == 0:
            return False
        i = 0
        while i < num_length - i - 1:
            if num_string[i] != num_string[num_length - i - 1]:
                return False
            i = i + 1
        return True

    def prime_palindrome(n: int) -> int:
        answer = n
        if answer <= 2:
            return 2
        if 7 < answer <= 11:
            return 11
        if answer % 2 == 0:
            answer = answer + 1
        while True:
            num_length = len(str(answer))
            if num_length % 2 == 0:
                answer = 10 ** num_length + 1
                continue
            elif Solution.is_palindrome(answer) and Solution.is_prime(answer):
                return answer
            answer = answer + 2

    def primePalindrome(self, N: int) -> int:
        return Solution.prime_palindrome(N)
