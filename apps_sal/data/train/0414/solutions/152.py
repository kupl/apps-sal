class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        maxsofar = arr[0]
        for i in range(len(arr)):
            wins = 0
            if arr[i] > maxsofar:
                wins += 1
                maxsofar = arr[i]
            for j in range(i + 1, len(arr)):
                if wins == k:
                    return arr[i]
                if arr[j] > arr[i]:
                    break
                else:
                    wins += 1
        return maxsofar
