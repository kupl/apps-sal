class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def at_most(k):
            start_ptr = 0
            result = 0

            for end_ptr in range(len(nums)):
                k -= nums[end_ptr] % 2

                while k < 0:
                    k += nums[start_ptr] % 2
                    start_ptr += 1

                result += end_ptr - start_ptr + 1

            return result

        return at_most(k) - at_most(k - 1)
