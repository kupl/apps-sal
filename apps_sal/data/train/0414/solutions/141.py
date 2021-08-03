class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        wins = {}
        if k > len(arr):
            return max(arr)
        maximum = max(arr)
        index = 1
        while index < len(arr):
            maxi = max(arr[0], arr[index])
            mini = min(arr[0], arr[index])
            arr[0] = maxi
            index += 1
            if wins.get(maxi):
                wins[maxi] += 1
            else:
                wins[maxi] = 1
            if wins[maxi] == k:
                return maxi
            if arr[0] == maximum:
                return maximum
