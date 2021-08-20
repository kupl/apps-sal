class Solution:

    def countTriplets(self, nums):
        count_map = collections.Counter((i & j for i in nums for j in nums))
        return sum((count_map[key] for num in nums for key in count_map if num & key == 0))
