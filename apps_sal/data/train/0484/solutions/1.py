class Solution:
    
    def next_palindrome(self,n):
        if self.AreAll9s(n):
            pal = str(1)  
            for i in range(1, len(str(n))):  
                pal = pal + str(0)  
            pal = pal + str(1)
            return int(pal)
            
        x = len(str(n))
        if x>2:
            first_num = n//10**(x-1)
            if x%2==0:
                pal = str(1)
                for i in range(1, len(str(n))):
                    pal = pal + str(0)
                pal = pal + str(1)
                return int(pal)
            if first_num%2==0 or first_num%5==0:
                n = (first_num+1) * (10**(x-1))
            
        if x%2 == 0:
            first_half = n//(10**(x//2))
            first_half_reversed = str(first_half)[::-1]
            second_half = n%(10**(x//2))
            if int(first_half_reversed) > second_half:
                return int(str(first_half)+first_half_reversed)
            else:
                first_half = first_half + 1
                pal = str(first_half)+str(first_half)[::-1]
                return int(pal)
            
        else:
            first_half = n//(10**(x//2))
            second_half = n%(10**x//2)
            first_half_reversed = str(first_half//10)[::-1]
            if int(first_half_reversed) > second_half:
                return int(str(first_half)+first_half_reversed)
            else:
                first_half = first_half + 1
                pal = str(first_half)+str(first_half//10)[::-1]
                return int(pal)
            
        
    def AreAll9s(self,  n):  
        for i in str(n): 
            if( int(i) != 9 ) : 
                return 0
        return 1
    
    def mrange(self, start, stop, step):
        while start < stop:
            yield start
            start += step
        
    def check_prime(self, num):
        if num == 2:
            return True
        if (num < 2) or (num % 2 == 0):
            return False
        return all(num % i for i in self.mrange(3, int((num)**0.5) + 1, 2))
    
    def primePalindrome(self, N: int) -> int:
        x = N
        while x>=N:
            if x>11:
                x = self.next_palindrome(x)
                if self.check_prime(x):
                    return x
            else:
                if self.check_prime(x):
                    return x
                x= x+1
            
        
        

