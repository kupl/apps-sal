class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        candidates = arr[1:]
        winner = arr[0]
        nwin = 0
        while nwin < k and candidates:
            if winner > candidates[0]:
                nwin += 1
            else:
                winner = candidates[0]
                nwin = 1
            candidates.pop(0)
        return winner
