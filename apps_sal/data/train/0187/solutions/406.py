class Solution:
    def minOperationsMaxProfit(self, arr: List[int], b: int, r: int) -> int:
        best = [0, -1]
        cur = 0
        wait = 0
        i = 0
        while wait > 0 or i < len(arr):
            if i < len(arr):
                wait += arr[i]
            cur -= r
            board = min(4, wait)
            cur += b * board
            wait -= board
            i += 1
            if cur > best[0]:
                best = [cur, i]
        return best[1]
