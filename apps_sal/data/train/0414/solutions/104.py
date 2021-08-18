class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n:
            return max(arr)
        win_count = {}
        for i in arr:
            win_count[i] = 0

        count = 0

        while count != k:

            if arr[0] > arr[1]:
                win_index = 0
                lost_index = 1
            else:

                win_index = 1
                lost_index = 0

            lost = arr.pop(lost_index)
            arr.append(lost)

            win_count[arr[-1]] = 0
            win_count[arr[0]] += 1
            count = win_count[arr[0]]

        return arr[0]
