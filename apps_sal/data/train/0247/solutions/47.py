class Solution:

    def getArraysx(self, arr, target):
        leftSizes = {}
        rightSizes = {}
        posleft = 0
        posright = 0
        currSum = 0
        while posright < len(arr):
            currSum += arr[posright]
            if currSum == target:
                rightList = rightSizes.get(posleft, [])
                rightList.append(posright - posleft + 1)
                rightSizes[posleft] = rightList
                if posright + 1 < len(arr):
                    leftList = leftSizes.get(posright + 1, [])
                    leftList.append(posright - posleft + 1)
                    leftSizes[posright + 1] = leftList
                posright += 1
                currSum -= arr[posleft]
                posleft += 1
            elif currSum > target:
                currSum = currSum - arr[posright] - arr[posleft]
                posleft += 1
            else:
                posright += 1
        leftArray = [0] * len(arr)
        fullList = []
        for i in range(len(arr)):
            additional = leftSizes.get(i, [])
            fullList.extend(additional)
            if len(fullList) > 0:
                leftArray[i] = min(fullList)
            else:
                leftArray[i] = -1
        rightArray = [0] * len(arr)
        fullList = []
        for j in range(len(arr) - 1, -1, -1):
            additional = rightSizes.get(j, [])
            fullList.extend(additional)
            if len(fullList) > 0:
                rightArray[j] = min(fullList)
            else:
                rightArray[j] = -1
        return (leftArray, rightArray)

    def updateArrays(self, leftSizes, rightSizes, posleft, posright, maxvalue):
        value = rightSizes.get(posleft, maxvalue)
        rightSizes[posleft] = min(value, posright - posleft + 1)
        if posright + 1 < maxvalue:
            value = leftSizes.get(posright + 1, maxvalue)
            leftSizes[posright + 1] = min(value, posright - posleft + 1)

    def getArrays(self, arr, target):
        leftArray = [0] * len(arr)
        rightArray = [0] * len(arr)
        leftSizes = {}
        rightSizes = {}
        posleft = 0
        posright = 0
        currSum = 0
        while posright < len(arr):
            currSum += arr[posright]
            if currSum == target:
                self.updateArrays(leftSizes, rightSizes, posleft, posright, len(arr))
                posright += 1
                currSum -= arr[posleft]
                posleft += 1
            elif currSum > target:
                currSum = currSum - arr[posright] - arr[posleft]
                posleft += 1
            else:
                posright += 1
        leftArray = [len(arr)] * len(arr)
        for i in range(1, len(arr)):
            minValue = leftSizes.get(i, len(arr))
            leftArray[i] = min(minValue, leftArray[i - 1])
        rightArray = [len(arr)] * len(arr)
        for j in range(len(arr) - 1, -1, -1):
            minValue = rightSizes.get(j, len(arr))
            if j == len(arr) - 1:
                rightArray[j] = minValue
            else:
                rightArray[j] = min(minValue, rightArray[j + 1])
        return (leftArray, rightArray)

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        (leftArray, rightArray) = self.getArrays(arr, target)
        minSum = 2 * len(arr)
        for i in range(1, len(arr)):
            if leftArray[i] < len(arr):
                leftSize = leftArray[i]
            else:
                continue
            if rightArray[i] < len(arr):
                rightSize = rightArray[i]
            else:
                continue
            minSum = min(minSum, leftSize + rightSize)
        if minSum == 2 * len(arr):
            minSum = -1
        return minSum

    def minSumOfLengthsx(self, arr: List[int], target: int) -> int:
        posleft = 0
        posright = 0
        lengths = []
        currSum = 0
        while posright < len(arr):
            currSum += arr[posright]
            if currSum == target:
                lengths.append(posright - posleft + 1)
                posright += 1
                posleft = posright
                currSum = 0
            elif currSum > target:
                currSum = currSum - arr[posright] - arr[posleft]
                posleft += 1
            else:
                posright += 1
        print(lengths)
        if len(lengths) < 2:
            return -1
        lengths.sort()
        return sum(lengths[0:2])
