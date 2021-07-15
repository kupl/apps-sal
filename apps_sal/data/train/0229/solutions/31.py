class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        cnt = collections.Counter(A)
        # It handles the case where there is odd number of 0, since the total number is even, there should be a number which cannot match because of the extra 0
        for k in sorted(cnt, key=abs):
            if cnt[k] > cnt[2*k]:
                return False
            
            cnt[2*k] -= cnt[k]
            
        return True
