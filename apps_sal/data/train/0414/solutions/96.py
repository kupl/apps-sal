class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n:
            return max(arr)

        count = 1

        winner = arr[0] if arr[0] > arr[1] else arr[1]

        if winner == arr[0]:
            arr.insert(n - 1, arr.pop(1))

        else:
            arr.insert(n - 1, arr.pop(0))

        while count < k:
            if winner > arr[1]:
                arr.insert(-1, arr.pop(1))
                count += 1

            else:
                winner = arr[1]
                arr.insert(-1, arr.pop(0))
                count = 1

        return winner
