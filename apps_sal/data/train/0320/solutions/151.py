class Solution:

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        one = 0
        two_req = 0
        for i in nums:
            two = 0
            i_copy = i
            while i_copy > 0:
                if i_copy % 2 == 0:
                    i_copy = i_copy // 2
                    two += 1
                else:
                    i_copy -= 1
                    one += 1
            two_req = max(two_req, two)
        res = two_req + one
        return res
