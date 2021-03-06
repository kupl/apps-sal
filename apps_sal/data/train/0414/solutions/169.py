class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        cur = arr[0]
        win = 0
        for i in range(1, len(arr)):
            if arr[i] > cur:
                cur = arr[i]
                win = 0
            win += 1
            if win == k:
                break
        return cur
        widx = 0
        gen = (i for (i, x) in enumerate(arr) if x > arr[widx] and k >= i > 0)
        i = next(gen, None)
        if i:
            widx = i
        else:
            return arr[widx]
        while widx < len(arr):
            gen = (i for (i, x) in enumerate(arr) if x > arr[widx] and k > i - widx > 0)
            i = next(gen, None)
            if i:
                widx = i
            else:
                return arr[widx]
        win = cnt = 0
        for (i, x) in enumerate(arr):
            if win < x:
                (win, cnt) = (x, 0)
            if i:
                cnt += 1
            if cnt == k:
                break
        return win
