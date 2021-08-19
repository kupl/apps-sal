class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        count = 0
        current_max = arr[0]
        k = min(len(arr), k)
        for num in arr[1:]:
            if num > current_max:
                current_max = num
                count = 1
            else:
                count += 1
            if count >= k:
                return current_max
        return current_max
