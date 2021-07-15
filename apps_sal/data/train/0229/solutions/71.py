class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        
        
        ## Time Complexity: O(N LOG N) , Space: O(N)
        count = collections.Counter(A)
        for x in sorted(A, key = abs):
            if count[x] == 0: continue
            if count[2*x] == 0: return False
            count[x] -= 1
            count[2*x] -= 1

        return True

