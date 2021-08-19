class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        def cnt(tot, arr):
            mp = {}
            ans = 0
            for val in arr:
                if tot % val == 0 and tot / val in mp:
                    ans += mp[tot / val]
                mp[val] = mp.get(val, 0) + 1
            return ans

        def helper(arr1, arr2):
            last_num = None
            last_ans = None
            ans = 0
            for num in arr1:
                if num == last_num:
                    ans += last_ans
                else:
                    last_num = num
                    last_ans = cnt(num * num, arr2)
                    ans += last_ans
            return ans
        return helper(nums1, nums2) + helper(nums2, nums1)
