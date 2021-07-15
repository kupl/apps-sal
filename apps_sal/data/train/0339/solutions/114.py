from collections import defaultdict
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def solve(aa,bb):
            res=0
            cnt=defaultdict(int)
            for a in aa:
                for b in bb:
                    b2=b*b
                    if b2%a:continue
                    res+=cnt[b*b//a]
                cnt[a]+=1
            return res
        
        ans=solve(nums1,nums2)+solve(nums2,nums1)
        return ans

