class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        if len(arr) < k:
            return max(arr)
        count = collections.Counter(arr)
        inc = 1
        while True:
            winner = arr[0]
            if arr[0] < arr[1]:
                temp = arr[0]
                arr[0] = arr[1]
                arr[1] = temp
                winner = arr[0]
            temp = arr[1 + inc]
            arr[1 + inc] = arr[1]
            arr[1] = temp
            inc = (inc + 1) % (len(arr) - 1)
            count[winner] += 1
            if count[winner] == k + 1:
                return winner
