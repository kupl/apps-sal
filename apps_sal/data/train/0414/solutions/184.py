class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        ki = 0
        best = arr[0]
        for i in range(1, len(arr)):
            if arr[i] < best:
                ki += 1
            else:
                best = arr[i]
                ki = 1
            if ki == k:
                return best
        return best
