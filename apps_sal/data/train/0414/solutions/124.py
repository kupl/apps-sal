class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        win = cnt = 0
        for i, x in enumerate(arr):
            if win < x:
                win, cnt = x, 0
            if i:
                cnt += 1
            if cnt == k:
                break
        return win
