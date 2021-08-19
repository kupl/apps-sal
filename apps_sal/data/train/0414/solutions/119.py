class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        max_temp = arr[0]
        rounds = 0
        for i in range(1, len(arr)):
            if arr[i] > max_temp:
                rounds = 1
                max_temp = arr[i]
            else:
                rounds += 1
            if rounds == k:
                return max_temp
        return max(arr)
