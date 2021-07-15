class Solution:
    def canArrange(self, A: List[int], K: int) -> bool:
        counts = [0]*K
        
        for num in A:
            counts[num % K] += 1
        
        for x in range(K):
            y = -x % K
            while counts[x]:
                counts[x] -= 1
                counts[y] -= 1
                
                if counts[y] < 0:
                    return False
                
        return True
