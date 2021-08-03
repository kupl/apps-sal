class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        if not nums:
            return 0

        splittedArrays = []

        currentArray = []
        negCount = 0
        for num in nums:
            if num == 0:
                if len(currentArray) > 0:
                    splittedArrays.append((currentArray, negCount))
                currentArray = []
                negCount = 0
            else:
                currentArray.append(num)
                negCount += 1 if num < 0 else 0

        if len(currentArray) > 0:
            splittedArrays.append((currentArray, negCount))

        if not splittedArrays:
            return 0

        maxLength = 0
        for splittedArray, negCount in splittedArrays:
            if negCount % 2 == 0:
                maxLength = max(maxLength, len(splittedArray))
            else:
                removedNums = 0
                i = 0
                while splittedArray[i] > 0:
                    removedNums += 1
                    i += 1
                maxLength = max(maxLength, len(splittedArray) - removedNums - 1)

                removedNums = 0
                i = len(splittedArray) - 1
                while splittedArray[i] > 0:
                    removedNums += 1
                    i -= 1
                maxLength = max(maxLength, len(splittedArray) - removedNums - 1)

        return maxLength
