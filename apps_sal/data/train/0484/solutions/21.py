class Solution:
    def primePalindrome(self, N: int) -> int:
        def even_palindrome(n: int) -> int:
            return int(str(n) + str(n)[::-1])
        
        def odd_palindrome(n: int) -> int:
            return int(str(n) + str(n)[::-1][1:])
        
        def is_prime(n: int) -> int:
            return n > 1 and all(n%i for i in range(2, int(n**.5)+1))
        
        odd, even = 1, 1
        while True:
            next_even = even_palindrome(even)
            next_odd = odd_palindrome(odd)
            # print(next_even, next_odd)
            cur = min(next_even, next_odd)
            if cur >= N and is_prime(cur):
                return cur
            if next_even > next_odd:
                odd += 1
            else:
                even += 1        
