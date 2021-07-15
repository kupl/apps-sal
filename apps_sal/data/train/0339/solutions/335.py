from collections import Counter

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_products = productCounts(nums1)
        nums2_products = productCounts(nums2)
        nums1_squares = squareCounts(nums1)
        nums2_squares = squareCounts(nums2)

        result = 0
        for square, count in nums1_squares.items():
            result += count * nums2_products[square]

        for square, count in nums2_squares.items():
            result += count * nums1_products[square]

        return result

def productCounts(arr):
    result = Counter()
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            result.update((arr[i] * arr[j],))
    return result

def squareCounts(arr):
    result = Counter()
    for num in arr:
        result.update((num ** 2,))
    return result
