class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        result = 0
        negativeIndices = []
        currentProduct = 1
        startIndex = 0

        for index, number in enumerate(nums):
            if number == 0:
                negativeIndices = []
                currentProduct = 1
                startIndex = index + 1
                continue

            if number * currentProduct > 0:
                result = max(result, index - startIndex + 1)
                currentProduct = 1

            else:
                if len(negativeIndices) != 0:
                    result = max(result, index - negativeIndices[0])
                currentProduct = -1

            if number < 0 and len(negativeIndices) == 0:
                negativeIndices.append(index)

        return result
