class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n:
            return max(arr)
        cur = arr[0]
        win = 0
        for i in range(1, n):
            if arr[i] > cur:
                win = 0
                cur = arr[i]
            win += 1
            if win == k:
                break
        return cur
