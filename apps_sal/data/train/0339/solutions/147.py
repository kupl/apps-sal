class Solution:
    def calculate(self, nums1, nums2):
        a = [0] * 100001
        for i in nums1:
            a[i] += 1
        ans = 0
        for num in nums2:
            for i in nums1:
                if num * num % i == 0 and num * num // i <= 100000:
                    ans += a[num * num // i]
                    if num == i:
                        ans -= 1
        ans = ans // 2
        return ans
        
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        return self.calculate(nums1, nums2) + self.calculate(nums2, nums1)
