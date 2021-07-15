class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counts = Counter([x%k for x in arr])
        
        for key in counts:
            if key == 0 or key*2 == k:
                if counts[key] % 2:
                    return False
            elif counts[key] != counts[k-key]:
                    return False
            
            
        return True

