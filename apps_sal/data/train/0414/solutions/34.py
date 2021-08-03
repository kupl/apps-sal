class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:

        #n = len(arr)
        # if k>n: return max(arr)

        i = 0
        j = 1
        while True:
            if not i:
                m = k
            else:
                m = k - 1
            while j < len(arr) and arr[j] < arr[i]:
                m -= 1
                j += 1
            if m <= 0 or j >= len(arr):
                return arr[i]
            i += 1
            j = i + 1
