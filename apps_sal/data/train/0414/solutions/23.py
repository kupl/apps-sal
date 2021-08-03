class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:

        count = cur_ind = 0

        for i in range(len(arr) - 1):
            if arr[cur_ind] > arr[i + 1]:
                count += 1
            else:
                count = 1
                cur_ind = i + 1
            if count >= k:
                return arr[cur_ind]

        return arr[cur_ind]
