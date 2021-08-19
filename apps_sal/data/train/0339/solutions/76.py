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

    def numTriplets1(self, nums1: List[int], nums2: List[int]) -> int:
        counter = 0
        counter += self.wrapper(nums1, nums2)
        counter += self.wrapper(nums2, nums1)
        return counter

    def get_tables(self, nums):
        squares = {}
        products = {}
        i = 0
        while i != len(nums):
            j = i
            while j != len(nums):
                product_or_square = nums[i] * nums[j]
                if i == j:
                    if product_or_square not in squares:
                        squares[product_or_square] = 1
                    else:
                        squares[product_or_square] += 1
                elif product_or_square not in products:
                    products[product_or_square] = 1
                else:
                    products[product_or_square] += 1
                j += 1
            i += 1
        return (products, squares)

    def get_counts(self, products, squares):
        counter = 0
        if len(products) > len(squares):
            for square in list(squares.keys()):
                if square in products:
                    counter += squares[square] * products[square]
        else:
            for product in list(products.keys()):
                if product in squares:
                    counter += products[product] * squares[product]
        return counter

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        (products1, squares1) = self.get_tables(nums1)
        (products2, squares2) = self.get_tables(nums2)
        counter = 0
        counter += self.get_counts(products1, squares2)
        counter += self.get_counts(products2, squares1)
        return counter
