from math import sqrt


class Solution:
    def primePalindrome(self, N: int) -> int:
        ans = 9999999999
        MAX_K = 20_000

        if 8 <= N <= 11:
            return 11

        for i in range(2, MAX_K):
            # no need for even as would be div by 11
            o = make_odd_palindrome(i)
            if o >= N and is_prime(o):
                return o

        return ans


def make_odd_palindrome(n: int) -> int:
    s = str(n)
    p = s[:-1]
    odd = int(p + s[-1] + p[::-1])
    return odd


def is_prime(n: int) -> bool:
    for i in range(2, int(sqrt(n)) + 5):
        if n % i == 0 and n != i:
            return False

    return True
