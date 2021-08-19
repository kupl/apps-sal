class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
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
