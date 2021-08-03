class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        curMax = arr[0]
        numberOfWin = 0
        for i in range(1, len(arr)):
            if arr[i] > curMax:
                curMax = arr[i]
                numberOfWin = 0
            numberOfWin += 1
            if numberOfWin == k:
                break
        return curMax
