class Solution:
    def minOperations(self, n: int) -> int:

        generatedArray = []

        for i in range(n):
            generatedArray.append((2 * i) + 1)

        arrayLength = len(generatedArray)

        noOperations = 0

        # if arrayLength % 2 != 0:
        #     targetNumber = generatedArray[int(arrayLength // 2)]
        # else:
        #     targetNumber = generatedArray[int(arrayLength // 2) - 1] + 1

        for i in range(int(arrayLength // 2)):
            noOperations += (n - generatedArray[i])

        return noOperations
