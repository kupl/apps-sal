class Solution:

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:

        def getMaximumSum(subArr, t):
            subArrT = subArr.copy()
            for i in range(t - 1):
                subArrT.extend(subArr)
            nS = len(subArrT)
            maxSum = 0
            rSum = 0
            for i in range(nS):
                if rSum + subArrT[i] < 0:
                    rSum = 0
                    continue
                else:
                    rSum += subArrT[i]
                    if rSum > maxSum:
                        maxSum = rSum
            return maxSum

        def getHeadSum(subArr):
            headSum = 0
            nS = len(subArr)
            rSum = 0
            for i in range(nS):
                rSum += subArr[i]
                if rSum > headSum:
                    headSum = rSum
            return headSum
        headSum = getHeadSum(arr)
        tailSum = getHeadSum(arr[::-1])
        sumArr = sum(arr)
        result = 0
        if sumArr > 0:
            if k == 1:
                result = getMaximumSum(arr, 1)
            elif k == 2:
                result = tailSum + headSum
            else:
                result = tailSum + (k - 2) * sumArr + headSum
        else:
            if k > 1:
                if headSum + tailSum > result:
                    result = headSum + tailSum
            if getMaximumSum(arr, 1) > result:
                result = getMaximumSum(arr, 1)
        return result % (10 ** 9 + 7)
