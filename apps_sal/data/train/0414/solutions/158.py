class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr) - 1:
            return max(arr)

        widx = 0
        i = next((i for i, x in enumerate(arr) if x > arr[widx] and k >= i > 0), None)
        if i == None:
            return arr[widx]
        else:
            widx = i
        while widx < len(arr):
            i = next((i for i, x in enumerate(arr) if x > arr[widx] and k > i - widx > 0), None)
            print(i)
            if i == None:
                return arr[widx]
            else:
                widx = i
