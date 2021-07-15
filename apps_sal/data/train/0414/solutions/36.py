class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        max_arr = max(arr)
        max_arr_idx = arr.index(max_arr)
        if k >= max_arr_idx:
            return max(arr)
        if k <=1:
            return max(arr[0], arr[1])

        last_winner = None
        count = 0
        while True:

            if arr[0] > arr[1]:
                winner = arr[0]
                loser = arr[1]
            else:
                winner = arr[1]
                loser = arr[0]
            arr.remove(loser)
            arr.append(loser)
            if last_winner == winner:
                count += 1
                if count >= k - 1:
                    return arr[0]
            else:
                count = 0
                last_winner = winner    

