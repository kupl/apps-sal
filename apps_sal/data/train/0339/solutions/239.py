class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        return self.calc(nums1, nums2) + self.calc(nums2, nums1)

    def calc(self, nums1, nums2):
        d, ans = defaultdict(int), 0
        for num in nums2:
            d[num] += 1
        for i, num1 in enumerate(nums1):
            visited = {num: False for num in d}
            for num2 in d:
                cnt2 = d[num2]
                if visited[num2]:
                    continue
                if num1 * num1 % num2 == 0 and num1 * num1 // num2 in d:
                    num3, cnt3 = num1 * num1 // num2, d[num1 * num1 // num2]
                    ans += cnt2 * cnt3 if num2 != num3 else cnt2 * (cnt2 - 1) // 2
                    visited[num3] = True
                    visited[num2] = True
        return ans
