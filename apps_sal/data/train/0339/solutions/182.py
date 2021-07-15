class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        def cal(n, nums):
            nonlocal ans
            d = defaultdict(int)
            for num in nums:
                if n % num == 0:
                    ans += d[n/num]
                d[num] += 1
            
        for n in nums1:
            cal(n*n, nums2)
        for n in nums2:
            cal(n*n, nums1)
            
        return ans
