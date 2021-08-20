class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        halfLength = len(arr) // 2
        valDict = {}
        for val in arr:
            if val in valDict:
                valDict[val] += 1
            else:
                valDict[val] = 1
        setSize = 0
        lengthValsRemoved = 0
        for val in sorted(valDict.values(), reverse=True):
            setSize += 1
            lengthValsRemoved += val
            if lengthValsRemoved >= halfLength:
                break
        return setSize
