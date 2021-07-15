class Solution:
    def countTriplets(self, A: List[int]) -> int:
        counter = collections.Counter()
        
        for i in A:
            for j in A:
                counter[i&j] += 1
        
        result = 0        
        for k in A:
            for v in counter:
                if k & v == 0:
                    result += counter[v]
        return result
