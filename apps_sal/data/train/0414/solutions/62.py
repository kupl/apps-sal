class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if len(arr) <= 1:
            return 0
        a = arr[::]
        a.sort()
        maxi = a[-1]
        a.clear()
        winner = -1 * 2**32
        winCount = 0
        while winCount < k:
            #print(winCount, arr, winner)
            if arr[0] == maxi or arr[1] == maxi:
                return maxi
            if arr[0] < arr[1]:
                if arr[1] == winner:
                    winCount += 1
                else:
                    winCount = 1
                winner = arr[1]
                arr += [arr.pop(0)]
            else:
                if arr[0] == winner:
                    winCount += 1
                else:
                    winCount = 1
                winner = arr[0]
                arr += [arr.pop(1)]
        return winner
