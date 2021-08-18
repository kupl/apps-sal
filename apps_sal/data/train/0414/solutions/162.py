class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        original_length = len(arr)
        count = 0
        winner = 0
        curr = 1
        while count < k:
            if count > original_length:
                return arr[winner]
            if arr[winner] > arr[curr]:
                arr.append(arr[curr])
                curr += 1
                count += 1
            else:
                arr.append(arr[winner])
                winner = curr
                curr += 1
                count = 1
        return arr[winner]
