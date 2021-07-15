class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k>=len(arr):
            return max(arr)
        winner,win = arr.pop(0),0
        while True:
            temp = arr.pop(0)
            if temp>winner:
                arr.append(winner)
                winner,win = temp,1
            else:
                arr.append(temp)
                win += 1
            if win == k:
                return winner

