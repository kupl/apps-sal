class Solution:
    def wrapper(self, toSquare, toProd):

        # create a hash table of count of unique squared ints in arr 1
        table = {}
        for integer in toSquare:
            squared = integer**2
            if squared not in table:
                table[squared] = 1
            else:
                table[squared] += 1

        counter = 0
        # get all pairs products, check in hash table, if so, inc counter by count in table
        i = 0
        while i < len(toProd):  # minus one ok too?
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
