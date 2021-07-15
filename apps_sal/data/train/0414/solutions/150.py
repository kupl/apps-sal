class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr): return max(arr)
        i = 0
        while i < len(arr):
            kk = 0
            j = i
            while i+1< len(arr) and arr[i+1] < arr[j] and kk < k:
                i += 1
                kk += 1
            if kk == k: return arr[j]
            if kk == k-1 and j-1 >= 0 and arr[j-1] < arr[j]: return arr[j]
            if i+1 == len(arr) and j-1 >= 0 and arr[j-1] < arr[j]: return arr[j]
            if i == j: i += 1
        return -1
            

