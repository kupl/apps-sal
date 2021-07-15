import itertools
def calCross(nums):
    res = []
    pairs = list(itertools.combinations(nums,2))
    for (i,j) in pairs:
        res.append(i*j)
    return res

def commonCnt(nums1,nums2):
    res = 0
    cross = set(nums1)&set(nums2)
    for e in cross:
        res += nums1.count(e)*nums2.count(e)
    return res                    

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        square1 = [e*e for e in nums1]
        square2 = [e*e for e in nums2]
        cross1 = calCross(nums1)
        cross2 = calCross(nums2)
        res = commonCnt(square1, cross2)
        res += commonCnt(square2, cross1)
        return res
