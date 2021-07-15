from collections import defaultdict
class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        if not A:
            return True
        
        count = 0
        d = defaultdict(int)
        for i in A:
            d[i] += 1
        
        for num in sorted(A):
            if num*2 in d and d[num] and d[num*2]:
                d[num] -= 1
                d[num*2] -= 1
                count += 1
        
        return count == (len(A) // 2)


