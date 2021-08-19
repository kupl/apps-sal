class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n - 1:
            return max(arr)
        (winner, win_count) = (None, 0)
        c = 0
        while win_count < k:
            (p1, p2) = (arr[c], arr[(c + 1) % n])
            (w, l) = (max(p1, p2), min(p1, p2))
            if winner == w:
                win_count += 1
            else:
                (winner, win_count) = (w, 1)
            (arr[c], arr[(c + 1) % n]) = (l, w)
            c = (c + 1) % n
        return winner
