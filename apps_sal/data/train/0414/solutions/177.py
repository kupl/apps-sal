class Solution:
    def getWinner(self, arr, k):
        maxval = max(arr)
        l = len(arr)
        if k >= l - 1:
            return maxval
        win = False
        while True:
            if win:
                local_max = max(arr[:k])
            else:
                local_max = max(arr[:k + 1])
            if local_max == arr[0]:
                return local_max
            else:
                win = True
                index = arr.index(local_max)
                arr = arr[index:] + arr[:index]
