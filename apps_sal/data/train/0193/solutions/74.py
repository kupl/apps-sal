class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        numberDict = {}
        for i in range(len(arr)):
            if arr[i] not in numberDict:
                numberDict[arr[i]] = 1
            else:
                numberDict[arr[i]] += 1
        sortedOrders = sorted(list(numberDict.items()), key=lambda x: x[1], reverse=True)
        total = 0
        setSize = 0
        for i in sortedOrders:
            if total >= len(arr) // 2:
                return setSize
            total += i[1]
            setSize += 1
        return setSize
