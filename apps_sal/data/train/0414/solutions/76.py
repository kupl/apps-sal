class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k > len(arr) + 3:
            return max(arr)
        wins = 0
        win_num = arr[0]
        while wins < k:
            if arr[0] > arr[1]:
                if arr[0] == win_num:
                    wins += 1
                else:
                    wins = 1
                win_num = arr[0]
                arr.append(arr[1])
                arr.pop(1)
            else:
                if arr[1] == win_num:
                    wins += 1
                else:
                    wins = 1
                win_num = arr[1]
                arr.append(arr[0])
                arr.pop(0)

        return win_num
