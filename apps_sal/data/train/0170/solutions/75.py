class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        i = 1
        if len(arr) <= 1:
            return 0
        while i < n:
            if arr[i] < arr[i-1]:
                break
            i += 1
        max_len = i
        if max_len == n:
            return 0
        ini_ind = i - 1
        end_ind = 1
        while ini_ind >= 0:
            if arr[ini_ind] <= arr[-1]:
                break
            ini_ind -= 1
        max_len = max(max_len, ini_ind + end_ind + 1)
        while arr[-end_ind-1] <= arr[-end_ind]:
            while ini_ind >= 0:
                if arr[ini_ind] <= arr[-end_ind-1]:
                    break
                ini_ind -= 1
            end_ind += 1
            max_len = max(max_len, ini_ind + end_ind + 1)
        return n - max_len
