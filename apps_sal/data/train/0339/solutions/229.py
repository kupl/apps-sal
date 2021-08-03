class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def cnt(tot, arr):
            mp = {}
            ans = 0
            for val in arr:
                if tot % val == 0 and tot / val in mp:
                    ans += mp[tot / val]
                mp[val] = mp.get(val, 0) + 1
            return ans
        ans = 0
        for num in nums1:
            ans += cnt(num * num, nums2)
        for num in nums2:
            ans += cnt(num * num, nums1)
        return ans
