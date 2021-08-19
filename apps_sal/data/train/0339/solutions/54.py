class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        def numValid(target, nums):
            (start, end) = (0, len(nums) - 1)
            ans = 0
            while start < end:
                if target * target == nums[start] * nums[end]:
                    if nums[start] == nums[end]:
                        n = end - start + 1
                        ans += n * (n - 1) // 2
                        break
                    else:
                        start += 1
                        end -= 1
                        dup1 = dup2 = 1
                        while start < end and nums[start - 1] == nums[start]:
                            start += 1
                            dup1 += 1
                        start -= 1
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1
                            dup2 += 1
                        ans += dup1 * dup2
                elif target * target < nums[start] * nums[end]:
                    end -= 1
                elif target * target > nums[start] * nums[end]:
                    start += 1
            return ans
        ans = 0
        for num1 in nums1:
            ans += numValid(num1, nums2)
        for num2 in nums2:
            ans += numValid(num2, nums1)
        return ans
