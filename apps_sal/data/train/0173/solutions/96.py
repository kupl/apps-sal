class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # Stores count of remainders
        c = collections.Counter([i%k for i in arr])
        
        for j in c:
            # If reminder is 0
            # Check if this remainder is even
            if j == 0:
                if c[j]%2!=0: return False
            # If remainder is not 0
            # Check if current remainder c[j] is not equal to c[k-j], divisor-current remainder
            else:
                if c[j]!=c[k-j]:return False
        return True
