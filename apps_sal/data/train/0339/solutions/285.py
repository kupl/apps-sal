class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        res = 0
        for a in nums1:
            sq = a * a
            cnt = Counter()
            for b in nums2:
                if sq % b == 0 and sq//b in cnt:
                    res += cnt[sq//b]
                cnt[b] += 1
        
        for a in nums2:
            sq = a * a
            cnt = Counter()
            for b in nums1:
                if sq % b == 0 and sq//b in cnt:
                    res += cnt[sq//b]
                cnt[b] += 1
        return res
                    
        
        
        
        
        
        

