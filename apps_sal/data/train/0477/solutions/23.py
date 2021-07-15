class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        bits = [False]
        
        for i in range(1, n+1):
            bits.extend([True] + [j==False for j in bits[::-1]])
            
        return str(int(bits[k-1]))
