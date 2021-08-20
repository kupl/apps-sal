class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        indeces = {}
        for i in range(len(arr)):
            indeces[arr[i]] = i
        leftToRight = {}
        rightToLeft = {}
        result = -1
        numOfGroup = 0
        for i in range(len(arr)):
            num = arr[i]
            if rightToLeft.get(num - 1) is not None and leftToRight.get(num + 1) is not None:
                leftToRight[rightToLeft[num - 1]] = leftToRight[num + 1]
                rightToLeft[leftToRight[num + 1]] = rightToLeft[num - 1]
                if leftToRight[num + 1] - rightToLeft[num - 1] + 1 == m:
                    numOfGroup += 1
                if leftToRight.get(num + 1) - (num + 1) + 1 == m:
                    numOfGroup -= 1
                if num - 1 - rightToLeft.get(num - 1) + 1 == m:
                    numOfGroup -= 1
                leftToRight[num + 1] = None
                rightToLeft[num - 1] = None
            elif rightToLeft.get(num - 1) is not None:
                rightToLeft[num] = rightToLeft[num - 1]
                leftToRight[rightToLeft[num - 1]] = num
                if num - rightToLeft[num - 1] + 1 == m:
                    numOfGroup += 1
                if num - 1 - rightToLeft[num - 1] + 1 == m:
                    numOfGroup -= 1
                rightToLeft[num - 1] = None
            elif leftToRight.get(num + 1) is not None:
                leftToRight[num] = leftToRight[num + 1]
                rightToLeft[leftToRight[num + 1]] = num
                if leftToRight[num + 1] - num + 1 == m:
                    numOfGroup += 1
                if leftToRight[num + 1] - (num + 1) + 1 == m:
                    numOfGroup -= 1
                leftToRight[num + 1] = None
            else:
                leftToRight[num] = num
                rightToLeft[num] = num
                if m == 1:
                    numOfGroup += 1
            if numOfGroup > 0:
                result = i + 1
        return result
