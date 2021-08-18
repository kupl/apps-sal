from collections import Counter
import math


class Solution:
    def f(self, nums1, nums2):
        n1 = len(nums1)
        freq_dict_2 = Counter(nums2)
        answer = 0
        for pos_a, a in enumerate(nums1):
            for pos_b in range(pos_a + 1, n1):
                b = nums1[pos_b]
                c_square = a * b
                potential_c = math.floor(math.sqrt(c_square))
                if potential_c**2 == (c_square):
                    if potential_c in freq_dict_2:
                        answer += freq_dict_2[potential_c]
        return answer

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        final_answer = 0
        final_answer += self.f(nums1, nums2)
        final_answer += self.f(nums2, nums1)
        return final_answer
