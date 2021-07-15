from collections import Counter

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = Counter([0])
        
        ans = 0
        psum = 0
        for v in map(lambda x: x % 2, nums):
            psum += v
            ans += count[psum - k]
            count[psum] += 1
        
        return ans
