class Solution:
    def numTriplets(self, nums1, nums2):
        mp1, mp2 = {}, {}
        for ele in nums1:
            if ele in mp1: mp1[ele] += 1
            else: mp1[ele] = 1
        for ele in nums2:
            if ele in mp2: mp2[ele] += 1
            else: mp2[ele] = 1
        
        ans = 0
        for k1, v1 in mp1.items():
            tar = k1 ** 2
            for k2 in sorted(mp2.keys()):
                if k2 ** 2 > tar: break
                elif k2 ** 2 == tar:
                    ans += v1 * mp2[k2] * (mp2[k2] - 1) // 2
                elif tar % k2 == 0 and (tar // k2) in mp2:
                    ans += v1 * mp2[k2] * mp2[tar // k2]
        for k2, v2 in mp2.items():
            tar = k2 ** 2
            for k1 in sorted(mp1.keys()):
                if k1 ** 2 > tar: break
                elif k1 ** 2 == tar:
                    ans += v2 * mp1[k1] * (mp1[k1] - 1) // 2
                elif tar % k1 == 0 and (tar // k1) in mp1:
                    ans += v2 * mp1[k1] * mp1[tar // k1]
        return ans
