class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        consecutiveWins = 0
        champion = arr[0]
        hefty = max(arr)

        while consecutiveWins != k:
            if champion == hefty:
                return hefty

            if arr[0] > arr[1]:
                arr.append(arr.pop(1))

            elif arr[0] < arr[1]:
                arr.append(arr.pop(0))

            if arr[0] == champion:
                consecutiveWins += 1
            else:
                champion = arr[0]
                consecutiveWins = 1

        return champion
