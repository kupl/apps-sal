class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        checkSet = OrderedDict()
        windowStart = 0 
        count = 0
        ans = []
        for i, n in enumerate(A):
            checkSet[n] = i
            checkSet.move_to_end(n)
            while len(checkSet) > K:
                windowStart = checkSet.popitem(last=False)[1] + 1
            if len(checkSet) == K:
                count += next(iter(list(checkSet.items())))[1]- windowStart +1
        return count
            
                

