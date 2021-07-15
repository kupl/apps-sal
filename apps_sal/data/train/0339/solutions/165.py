class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def twoProd(B, sq):
            d = defaultdict(int)
            cnt = 0
            for val in B:
                if sq % val == 0:
                    cnt += d.get(sq // val, 0)
                d[val] += 1
            return cnt
        
        def poss(A, B):
            ret = 0
            m, n = len(A), len(B)
            for x in A:
                ret += twoProd(B, x * x)
            return ret
        
        return poss(nums1, nums2) + poss(nums2, nums1)

