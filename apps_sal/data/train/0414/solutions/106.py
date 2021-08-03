class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n:
            return max(arr)

        winCount = 0
        winner = arr[0]

        while winCount != k:
            if arr[0] > arr[1]:
                if winner == arr[0]:
                    winCount += 1
                else:
                    winCount = 1
                winner = arr[0]
                arr.append(arr[1])
                arr.pop(1)
            else:
                if winner == arr[1]:
                    winCount += 1
                else:
                    winCount = 1

                winner = arr[1]
                arr.append(arr[0])
                arr.pop(0)
        return winner
