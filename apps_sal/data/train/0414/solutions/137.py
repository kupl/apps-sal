class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        winn_count = 0
        n = len(arr)
        i = 0
        while winn_count < k and i < n:
            print(winn_count)
            if arr[0] > arr[i]:
                winn_count += 1
            elif arr[0] < arr[i]:
                (arr[0], arr[i]) = (arr[i], arr[0])
                winn_count = 1
            i += 1
        return arr[0]
