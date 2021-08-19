class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        wins = 0
        currWinner = arr[0]
        for i in range(1, len(arr)):
            print(currWinner)
            if currWinner > arr[i]:
                wins += 1
            else:
                currWinner = arr[i]
                wins = 1
            if wins == k:
                return currWinner
        return currWinner
