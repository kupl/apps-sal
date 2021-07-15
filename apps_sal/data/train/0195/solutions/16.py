class Solution:
    def countTriplets(self, A: List[int]) -> int:
        counter = Counter()
        for a in A:
            for b in A:
                counter[a&b] += 1
        
        res = 0
        for a in A:
            for b in counter:
                if a&b==0:
                    res += counter[b]
                    
        return res
