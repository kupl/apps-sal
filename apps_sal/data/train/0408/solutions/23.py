class Solution:

    def findBestValue(self, arr: List[int], target: int) -> int:
        """
        sums = []
        for i in range(max(arr)+1):
            currSum = 0 
            for val in arr: 
                if val > i: 
                    currSum += i
                else:
                    currSum += val

            sums.append((abs(currSum-target),i))
        sums.sort(key = lambda x:x[0])
        return sums[0][1]
        """
        '\n        sums = []\n        for i in range(max(arr)+1):\n            currSum = 0 \n            for val in arr: \n                if val > i: \n                    currSum += i\n                else:\n                    currSum += val\n            if currSum-target > 0:\n                sums.append((abs(currSum-target),i))\n                break\n            else:\n                sums.append((abs(currSum-target),i))\n        sums.sort(key = lambda x:x[0])\n        return sums[0][1]\n        '
        "\n        def condition(cutoff): \n            currSum = 0\n            for val in arr: \n                if val > cutoff: \n                    currSum += cutoff\n                else:\n                    currSum += val\n            return abs(currSum - target)\n            \n        left, right = 0, target\n        currSum = (float('inf'), -1) #smallest sum, the cutoff value which gives you the smallest sum \n        while left <= right: \n            mid = left + (right - left) // 2\n            checkSum = condition(mid)\n            if checkSum < currSum[0]: #if the smallest sum is smaller than the previous smallest sum, store the cutoff value\n                currSum = (checkSum, mid)\n                right = mid - 1\n            else:\n                left = mid + 1\n            print(left, right)\n        return currSum[1]\n        "

        def condition(cutoff):
            currSum = 0
            for val in arr:
                if val > cutoff:
                    currSum += cutoff
                else:
                    currSum += val
            return currSum
        (left, right) = (0, max(arr))
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid) < target:
                left = mid + 1
            else:
                right = mid
        if abs(target - condition(left)) < abs(target - condition(left - 1)):
            return left
        else:
            return left - 1
