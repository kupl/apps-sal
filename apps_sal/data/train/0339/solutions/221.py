class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def generate_nums(nums):
            nums = sorted(list(collections.Counter(nums).items()))
            n = len(nums)
            pow_nums = defaultdict(int)
            mul_nums = defaultdict(int)
            for i in range(n):
                num = nums[i][0]
                pow_nums[num * num] += nums[i][1]
                for j in range(i + 1, n):
                    mul_nums[num * nums[j][0]] += nums[i][1] * nums[j][1]
                mul_nums[num * num] += nums[i][1] * (nums[i][1] - 1) // 2
            return (pow_nums, mul_nums)
        (pow_nums1, mul_nums1) = generate_nums(nums1)
        (pow_nums2, mul_nums2) = generate_nums(nums2)
        ans = 0

        def check_triplet(nums, pow_nums):
            ans = 0
            for (num, count) in nums.items():
                ans += pow_nums[num] * count
            return ans
        ans += check_triplet(mul_nums1, pow_nums2)
        ans += check_triplet(mul_nums2, pow_nums1)
        return ans
