class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def find(nums1,nums2):
            res=0
            for x in nums1:
                cnt=defaultdict(int)
                for y in nums2:
                    if (x*x)%y==0:
                        res+=cnt[(x*x)//y]
                    cnt[y]+=1
            return res
        ret=0
        ret+=find(nums1,nums2)
        ret+=find(nums2,nums1)
        return ret
