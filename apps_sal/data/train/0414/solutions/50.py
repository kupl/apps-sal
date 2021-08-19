class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        smaller = 0
        arrLen = len(arr)
        currIndex = 0
        for i in range(arrLen - 1):
            if smaller == k:
                return arr[currIndex]
            if arr[currIndex] > arr[i + 1]:
                smaller += 1
                continue
            smaller = 1
            currIndex = i + 1
        return arr[currIndex]
