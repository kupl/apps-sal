class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        i = 0
        j = 1
        bigger_than = 0
        len_arr = len(arr)
        while bigger_than < min(k, len_arr - 1):
            if arr[i] > arr[j % len_arr]:
                j += 1
                bigger_than += 1
            else:
                i = j
                j += 1
                bigger_than = 1
        return arr[i]
