class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # if k > len(arr)-1:
        #     return max(arr)
        candidates = arr[1:]
        winner = arr[0]
        nwin = 0
        while nwin < k and candidates:
            if winner > candidates[0]:
                nwin += 1
            else:
                winner = candidates[0]
                nwin = 1
            del candidates[0]
        return winner
