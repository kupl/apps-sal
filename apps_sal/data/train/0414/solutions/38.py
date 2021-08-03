import math


class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        def find_max(arr):
            max_num = -math.inf
            for i in arr:
                if i > max_num:
                    max_num = i
            return max_num

        if k >= len(arr) - 1:
            return find_max(arr)
        else:
            win_count = 0
            while True:
                if arr[0] < arr[1]:
                    arr.append(arr[0])
                    arr.pop(0)
                    win_count = 1
                else:
                    arr.append(arr[1])
                    arr.pop(1)
                    win_count += 1
                if win_count == k:
                    return arr[0]
