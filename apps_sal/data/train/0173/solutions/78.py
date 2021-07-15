class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counts = defaultdict(lambda:0)
        
        for n in arr:
            mod = n % k
            
            if counts[k - mod] == 0:
                counts[mod] += 1
            else:
                counts[k - mod] -= 1
                
        
        return counts[0] % 2 == 0 and sum(counts.values()) - counts[0] == 0
