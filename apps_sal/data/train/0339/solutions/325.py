class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        table1 = {}
        table2 = {}
        res = 0

        for n in nums1:
            square = n * n
            table = {}
            for j, m in enumerate(nums2):
                if square % m == 0:
                    remainder = square // m
                    if remainder in table:
                        # print(square, m, remainder, table)
                        res += table[remainder]
                if m not in table:
                    table[m] = 0
                table[m] += 1

        for n in nums2:
            square = n * n
            table = {}
            for j, m in enumerate(nums1):
                if square % m == 0:
                    remainder = square // m
                    if remainder in table:
                        # print(square, m, remainder, table)

                        res += table[remainder]
                if m not in table:
                    table[m] = 0
                table[m] += 1
        return res
