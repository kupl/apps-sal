class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def count(num, nums):
            m = {}
            cnt = 0
            for n in nums:
                if num%n == 0:
                    if m.get(num/n) is not None:
                        cnt += m[num/n]
                if m.get(n) is None:
                    m[n] = 1
                else:
                    m[n] += 1
            return cnt

        res = 0
        for num in nums1:
            res += count(num*num, nums2)
        for num in nums2:
            res += count(num*num, nums1)
        return res
