class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = list(set(arr2))
        arr2.sort()
        m, n = len(arr1), len(arr2)
        keep = [float('inf')] * m
        swap = [[float('inf') for _ in range(n)] for _ in range(m)]
        keep[0] = 0
        for i in range(n):
            swap[0][i] = 1
        for i in range(1, m):
            min_keep, min_swap = float('inf'), float('inf')
            for j in range(n):
                if j > 0:
                    min_swap = min(min_swap, swap[i - 1][j - 1] + 1)
                if arr1[i] > arr2[j]:
                    min_keep = min(min_keep, swap[i - 1][j])
                if arr1[i] > arr1[i - 1]:
                    keep[i] = keep[i - 1]
                if arr2[j] > arr1[i - 1]:
                    swap[i][j] = keep[i - 1] + 1
                keep[i] = min(keep[i], min_keep)
                swap[i][j] = min(swap[i][j], min_swap)
        s = float('inf')
        for i in range(n):
            s = min(s, swap[m - 1][i])
        res = min(s, keep[m - 1])
        return -1 if res >= float('inf') else res
