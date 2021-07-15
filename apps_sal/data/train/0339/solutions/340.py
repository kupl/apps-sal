from typing import List
import bisect
from math import comb


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        nums1.sort()
        nums2.sort()
        res += self.find(nums1, nums2)
        res += self.find(nums2, nums1)
        return res

    def find(self, n1, n2):
        res = 0
        for n in n1:
            left = 0
            right = len(n2) - 1
            while left < right:
                if n2[left] * n2[right] == n ** 2:
                    if n2[left] == n2[right]:
                        res += comb(right - left + 1, 2)
                        while left < right and n2[left] == n2[left + 1]:
                            left += 1
                        while left < right and n2[right] == n2[right - 1]:
                            right -= 1
                    else:
                        nl = 1
                        nr = 1
                        while left < right and n2[left] == n2[left + 1]:
                            nl += 1
                            left += 1
                        while left < right and n2[right] == n2[right - 1]:
                            nr += 1
                            right -= 1
                        res += nl * nr
                    left += 1
                    right -= 1

                elif n2[left] * n2[right] < n ** 2:
                    left += 1
                else:
                    right -= 1
        return res

