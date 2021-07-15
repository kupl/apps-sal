class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        
        main = list(map(Counter, [str(2**n) for n in range(0, 30)]))
        return any(Counter(str(N)) == mape for mape in main)
    
    
        1892
