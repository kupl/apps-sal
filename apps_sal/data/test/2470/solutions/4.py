class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        m = len(arr1)
        arr2 = list(set(arr2))
        arr2.sort()
        n = len(arr2)
        keep = [float('inf')] * m
        keep[0] = 0
        swap = [[float('inf') for j in range(n)] for i in range(m)]
        for j in range(n):
            swap[0][j] = 1
        for i in range(1, m):
            min_keep = float('inf')
            min_swap = float('inf')
            for j in range(0, n):
                if j > 0:
                    min_swap = min(min_swap, swap[i - 1][j - 1] + 1)
                if arr1[i] > arr2[j]:
                    min_keep = min(min_keep, swap[i - 1][j])
                if arr1[i] > arr1[i - 1]:
                    keep[i] = keep[i - 1]
                if arr2[j] > arr1[i - 1]:
                    swap[i][j] = keep[i - 1] + 1
                swap[i][j] = min(swap[i][j], min_swap)
                keep[i] = min(keep[i], min_keep)

        k = keep[-1]
        min_swap = min(swap[-1])
        ans = min(min_swap, k)
        return ans if ans < float('inf') else -1
