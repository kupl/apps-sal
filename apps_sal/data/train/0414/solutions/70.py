class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        r = 0
        l = len(arr)
        count = 0
        while True:
            count += 1
            if count > l:
                return arr[0]
            if arr[0] > arr[1]:
                r += 1
                if r == k:
                    return arr[0]
                temp = arr[1]
                arr.pop(1)
                N = len(arr)
                arr.insert(N, temp)
            else:
                r = 1
                if r == k:
                    return arr[1]
                temp = arr[0]
                arr.pop(0)
                N = len(arr)
                arr.insert(N, temp)
