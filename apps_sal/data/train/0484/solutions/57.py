def isPrime(val):
    if val == 1:
        return False
    if val == 2:
        return True
    if val % 2 == 0:
        return False
    for i in range(3, floor(sqrt(val)) + 2, 2):
        if val % i == 0:
            return False
    return True


class Solution:

    def primePalindrome(self, N: int) -> int:
        if N >= 8 and N <= 11:
            return 11
        mn = 1000000000.0
        for i in range(1, 10009):
            s = str(i)
            r = s[::-1]
            r = r[1:]
            t = int(s + r)
            if t >= N and isPrime(t):
                mn = min(mn, t)
        return mn
