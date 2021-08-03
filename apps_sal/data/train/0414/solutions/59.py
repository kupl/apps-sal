class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        res = 0
        win = arr[0]
        for n in arr[1:]:
            if n > win:
                win = n
                res = 0
            res += 1
            if res == k:
                break
        return win
