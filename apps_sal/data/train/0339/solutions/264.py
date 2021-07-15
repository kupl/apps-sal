class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        # x = [i for i in range(1000)]
        # y = [i for i in range(1000)]
        # ans = 0
        # for a in x:
        #     for b in y:
        #         ans += a*b % 1000000
        
        
        def cal(nums1, nums2):
            ans = 0
            for a in nums1:
                d = collections.defaultdict(lambda:0)
                sq = a*a
                for ib in range(0, len(nums2)):
                    b = nums2[ib]
                    if b == 0:
                        if a == 0:
                            ans += ib
                        else:
                            continue
                    if sq % b != 0:
                        continue
                    else:
                        c = sq/b
                        if c in d:
                            ans += d[c]
                    d[b] += 1
            print(ans)
            return ans
        
        return cal(nums1,nums2) + cal(nums2,nums1)
