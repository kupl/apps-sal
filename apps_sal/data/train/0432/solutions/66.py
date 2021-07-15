# O(nlogn) time and O(n) space, exactly the same as Q846: Hand of straights
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k: return False
        if k==1: return True
        
        n = len(nums)
        cnt = collections.Counter(nums)
        heapify(nums)
        
        for i in range(n//k):
            start = heappop(nums)
            while cnt[start] == 0:
                start = heappop(nums)
            
            for i in range(k):
                if cnt[start+i] == 0: return False
                cnt[start+i] -= 1
                
        return True

