def isPrimes(n):
    return n > 1 and all(n%d > 0 for d in range(2, int(sqrt(n)) + 1))

def reverse(x):
    ans = 0
    while x:
        ans = 10*ans + x%10
        x //= 10
    return ans

class Solution:
    def primePalindrome(self, N: int) -> int:
        if N >= 9989900:
            return 100030001
        while True:
            if N == reverse(N) and isPrimes(N):
                return N
            N += 1
        

