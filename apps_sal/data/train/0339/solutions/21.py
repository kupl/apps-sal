class Solution:

    def wrapper(self, toSquare, toProd):
        table = {}
        for integer in toSquare:
            squared = integer ** 2
            if squared not in table:
                table[squared] = 1
            else:
                table[squared] += 1
        counter = 0
        i = 0
        while i < len(toProd):
            j = i + 1
            while j < len(toProd):
                product = toProd[i] * toProd[j]
                if product in table:
                    counter += table[product]
                j += 1
            i += 1
        return counter

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        counter = 0
        counter += self.wrapper(nums1, nums2)
        counter += self.wrapper(nums2, nums1)
        return counter
