class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        wins = 0
        prev = arr[0]
        for cur in arr[1:]:
            if prev > cur:
                wins += 1
            else:
                prev = cur
                wins = 1
            if wins == k:
                return prev
        return max(arr)
