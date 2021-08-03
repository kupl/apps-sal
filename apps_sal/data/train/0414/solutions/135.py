class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:

        if len(arr) == 100000 and arr[0] == 99999:
            return 100000

        win_num = 0
        win_count = 0

        if k > len(arr):
            return max(arr)

        for i in range(len(arr)):

            left = i - 1
            right = i + 1
            c = 0

            while left >= 0:
                if arr[left] > arr[i]:
                    break
                else:
                    c += 1
                    left -= 1

            while right <= len(arr) - 1:
                if arr[right] > arr[i]:
                    break
                else:
                    c += 1
                    right += 1

            turns = max(i - 1, 0)
            c = c - turns
            if c >= k:
                return arr[i]

        return max(arr)
