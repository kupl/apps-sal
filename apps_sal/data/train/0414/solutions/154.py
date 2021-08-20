class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        win = cnt = 0
        for (i, x) in enumerate(arr):
            if win < x:
                (win, cnt) = (x, 0)
            if i:
                cnt += 1
            if cnt == k:
                break
        return win
        if k >= len(arr) - 1:
            return max(arr)
        widx = 0
        i = next((i for (i, x) in enumerate(arr) if x > arr[widx] and k >= i > 0), None)
        if i != None:
            widx = i
        else:
            return arr[widx]
        while widx < len(arr):
            i = next((i for (i, x) in enumerate(arr) if x > arr[widx] and k > i - widx > 0), None)
            print(i)
            if i != None:
                widx = i
            else:
                return arr[widx]
