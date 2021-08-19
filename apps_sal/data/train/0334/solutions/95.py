class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        output = []
        idx = 0
        while idx < len(s):
            char = s[idx]
            newIdx = idx + 1
            arr = [idx]
            while newIdx < len(s) and s[newIdx] == s[idx]:
                arr.append(newIdx)
                newIdx += 1
            idx = newIdx
            output.append(arr)
        totalCost = 0
        for newArr in output:
            if len(newArr) > 1:
                costArr = []
                for eachElem in newArr:
                    costArr.append(cost[eachElem])
                sortedArr = sorted(costArr, reverse=True)
                totalCost += sum(sortedArr[1:])
        return totalCost
