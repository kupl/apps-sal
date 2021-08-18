class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr) - 1:
            return max(arr)
        count = 0
        while count < k:
            if arr[0] > arr[1]:
                count += 1
                temp = arr[1]
                arr.remove(arr[1])
                arr.append(arr[1])
            else:
                count = 1
                arr.append(arr[0])
                arr = arr[1:]
        return arr[0]
