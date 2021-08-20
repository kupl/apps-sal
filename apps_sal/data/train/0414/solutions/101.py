class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        numWin = 0
        while numWin < k:
            if arr[0] < arr[1]:
                numWin = 1
                arr.append(arr.pop(0))
            else:
                numWin += 1
                arr.append(arr.pop(1))
        return arr[0]
