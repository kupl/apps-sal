class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        for num in nums1:
            ans += self.find_num_pairs(num, nums2)

        for num in nums2:
            ans += self.find_num_pairs(num, nums1)
        return ans

    def find_num_pairs(self, num, pair_list):
        pair_dict = {}
        square_num = num ** 2
        ans = 0
        for i, n in enumerate(pair_list):
            if square_num // n in pair_dict and square_num % n == 0:
                ans += len(pair_dict[square_num // n])
            if n not in pair_dict:
                pair_dict[n] = []
            pair_dict[n].append(i)

        return ans
