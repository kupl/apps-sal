class Solution:
    def primePalindrome(self, N: int) -> int:
        def isPrime(num):
            if num < 2 or num%2 == 0:
                return num ==2
            s_num = int(num**0.5)
            for i in range(3, s_num + 1):
                if num%i == 0:
                    return False
            return True
        
        
        if N>=8 and N <= 11:
            return 11
        
        for i in range(10 ** (len(str(N)) // 2), 10**5):
            s = str(i)
            s2 = s + s[::-1][1:]
            if isPrime(int(s2)) and int(s2)>= N:
                return int(s2)
        return N 
