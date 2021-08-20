class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        return self.num(nums1, nums2) + self.num(nums2, nums1)

    def num(self, nums1, nums2):
        possibleSquares = {}
        possibleProducts = {}
        for (idx, x) in enumerate(nums1):
            square = x * x
            if square in possibleSquares:
                possibleSquares[square].append(idx)
            else:
                possibleSquares[square] = [idx]
        for x in range(len(nums2) - 1):
            for y in range(x + 1, len(nums2)):
                product = nums2[x] * nums2[y]
                if product in possibleProducts:
                    possibleProducts[product].append((x, y))
                else:
                    possibleProducts[product] = [(x, y)]
        result = 0
        for s in possibleSquares:
            if s in possibleProducts:
                result += len(possibleSquares[s]) * len(possibleProducts[s])
        return result
