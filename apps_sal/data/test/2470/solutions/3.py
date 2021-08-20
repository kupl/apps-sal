import numpy as np


class Solution:

    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        m = len(arr1)
        arr2 = sorted(np.unique(arr2))
        n = len(arr2)
        keep = [float('inf')] * m
        keep[0] = 0
        swap = [1] * n
        for i in range(1, m):
            min_keep = float('inf')
            min_swap = float('inf')
            temp = [float('inf')] * n
            for j in range(n):
                if j > 0:
                    min_swap = min(min_swap, swap[j - 1] + 1)
                if arr1[i] > arr2[j]:
                    min_keep = min(min_keep, swap[j])
                if arr1[i] > arr1[i - 1]:
                    keep[i] = keep[i - 1]
                if arr2[j] > arr1[i - 1]:
                    temp[j] = keep[i - 1] + 1
                temp[j] = min(temp[j], min_swap)
                keep[i] = min(keep[i], min_keep)
            for j in range(n):
                (temp[j], swap[j]) = (swap[j], temp[j])
        s = min(swap)
        k = keep[-1]
        ans = min(s, k)
        return ans if ans < float('inf') else -1
