class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        highest = arr[0]
        wins = 0
        for a in arr[1:]:
            if highest > a:
                wins += 1
            else:
                highest = a
                wins = 1
            if wins == k:
                return highest
        return highest
