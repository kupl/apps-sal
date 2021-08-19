class Solution:

    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        m = len(arr1)
        arr2 = sorted(list(set(arr2)))
        n = len(arr2)
        swap = [[float('inf') for j in range(n)] for i in range(m)]
        keep = [float('inf') for i in range(m)]
        keep[0] = 0
        for j in range(n):
            swap[0][j] = 1
        for i in range(1, m):
            min_keep = float('inf')
            min_swap = float('inf')
            for j in range(n):
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
        res = min(min(swap[m - 1]), keep[m - 1])
        if res == float('inf'):
            return -1
        else:
            return res
