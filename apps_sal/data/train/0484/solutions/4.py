class Solution:
    def primePalindrome(self, N: int) -> int:
        if N == 1:
            return 2
        if N <= 3 or N ==5 or N == 7:
            return N
        if N == 4:
            return 5
        if N == 6:
            return 7
        if N <= 11:
            return 11
        
        
        for i in range(10, 2*10**4):
            s = str(i)
            num = int(s + s[:-1][::-1])
            if num >= N and self.is_prime(num):
                return num
        
    def is_prime(self, num):
        i = 2 
        while i*i <= num:
            if num%i == 0:
                return False
            i += 1
        return True
