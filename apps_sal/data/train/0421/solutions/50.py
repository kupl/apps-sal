class Solution:

    def lastSubstring(self, s: str) -> str:
        arrSize = len(s)
        suffArr = []
        for i in s:
            suffArr.append(ord(i))
        if len(list(set(suffArr))) == 1:
            print(len(s))
            return s
        sumArr = [0] * arrSize
        sumArr[-1] = suffArr[-1]
        for i in range(arrSize - 2, -1, -1):
            sumArr[i] = sumArr[i + 1] + suffArr[i]
        blockSize = 1
        currArr = suffArr[:]
        ret = 0
        while True:
            maxNum = max(currArr)
            maxInds = []
            for i in range(len(currArr)):
                if maxNum == currArr[i]:
                    maxInds.append(i)
            if len(maxInds) == 1:
                return str(s[maxInds[0]:])
            blockSize += 1
            for i in maxInds:
                if i + blockSize >= arrSize:
                    currArr[i] = sumArr[i]
                else:
                    currArr[i] = sumArr[i] - sumArr[i + blockSize]
        return None
