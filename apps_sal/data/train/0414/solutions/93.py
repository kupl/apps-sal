class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        first = arr[0]
        win_count = 0
        best_num = first
        while win_count != k:
            if first > arr[1]:
                win_count += 1
                if win_count == k:
                    best_num = first
                    break
                arr.append(arr.pop(1))
            else:
                win_count = 1
                arr.append(arr.pop(0))
                first = arr[0]
                if win_count == k:
                    best_num = first
                    break
        return best_num
