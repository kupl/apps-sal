class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        size1, size2 = len(arr1), len(arr2)
        Inf = float('inf')
        keep = [Inf] * size1
        keep[0] = 0
        swap = [[Inf] * size2 for _ in range(size1)]
        swap[0] = [1] * size2
        for i in range(1, size1):
            minKeep = minSwap = Inf
            for j in range(size2):
                if arr1[i] > arr1[i-1]:
                    keep[i] = keep[i-1]
                if arr1[i] > arr2[j]:
                    minKeep = min(minKeep, swap[i-1][j])
                if arr2[j] > arr1[i-1]:
                    swap[i][j] = keep[i-1] + 1
                if j > 0: # arr2[j] > arr2[j-1] is always True
                    minSwap = min(minSwap, swap[i-1][j-1] + 1)
                keep[i] = min(keep[i], minKeep)
                swap[i][j] = min(swap[i][j], minSwap)
        res = min(min(swap[-1]), keep[-1])
        return -1 if res == Inf else res

