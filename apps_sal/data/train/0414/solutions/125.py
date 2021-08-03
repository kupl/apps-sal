class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        win_count = 0
        cur_winner = arr[0]
        ptr1 = 0
        ptr2 = 1
        for i in range(0, len(arr)):
            winner = arr[ptr1] if arr[ptr1] > arr[ptr2] else arr[ptr2]
            if cur_winner == winner:
                win_count += 1
            else:
                cur_winner = winner
                win_count = 1
            if win_count == k:
                return winner
            ptr1 = ptr1 if arr[ptr1] > arr[ptr2] else ptr2
            ptr2 += 1
            if ptr2 == len(arr):
                ptr2 = 0
            if ptr2 == ptr1:
                ptr2 += 1
        return arr[ptr1]
