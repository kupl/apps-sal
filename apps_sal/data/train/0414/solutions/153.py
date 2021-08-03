class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winCnt = 0
        win = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[win]:
                winCnt += 1
                if winCnt >= k:
                    return arr[win]
            else:
                winCnt = 1
                win = i
                if winCnt >= k:
                    return arr[win]
        return arr[win]
