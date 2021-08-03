class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr) - 1:
            return max(arr)

        widx = 0  # current winner index
        i = next((i for i, x in enumerate(arr) if x > arr[widx] and k >= i > 0), None)
        if i != None:
            widx = i
        else:
            return arr[widx]

        while widx < len(arr):
            i = next((i for i, x in enumerate(arr) if x > arr[widx] and k > i - widx > 0), None)
            print(i)
            if i != None:
                widx = i
            else:
                return arr[widx]
