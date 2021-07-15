class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        countOfArray = Counter(arr)
        listOfValues = list(countOfArray.values())
        listOfValues.sort(reverse = True)
        lenOfArray = len(arr)
        halfTheLength = lenOfArray//2
        ret = 0
        for val in listOfValues:
            lenOfArray = lenOfArray - val
            ret += 1
            if lenOfArray <= halfTheLength :
                break
        return ret
