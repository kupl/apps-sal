class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        m1 = collections.defaultdict(int)
        m2 = collections.defaultdict(int)
        for (i, num) in enumerate(nums1):
            m1[num] += 1
        for (i, num) in enumerate(nums2):
            m2[num] += 1
        self.ans = 0

        def count(nums: List[int], m: dict) -> None:
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    prod = nums[i] * nums[j]
                    sqrt = math.sqrt(prod)
                    if sqrt in m:
                        self.ans += m[sqrt]
        count(nums1, m2)
        count(nums2, m1)
        return self.ans
