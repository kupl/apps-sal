class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        current = arr[0]
        wins = 0
        for i in range(1, n):
            if arr[i] > current:
                current = arr[i]
                wins = 0
            wins += 1
            if (wins == k):
                break
        return current
