class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        a = arr1
        b = sorted(list(set(arr2)))
        n, m = len(a), len(b)
        keep = [0, math.inf]
        swap = [[1] * m, [math.inf] * m]

        prev, curr = 1, 0
        for i in range(1, n):
            prev, curr = curr, prev
            swap[curr] = [math.inf] * m
            keep[curr] = math.inf
            if a[i] > a[i - 1]:
                keep[curr] = keep[prev]
            for j in range(m):
                if a[i] > b[j]:
                    keep[curr] = min(keep[curr], swap[prev][j])
                if b[j] > a[i - 1]:
                    swap[curr][j] = min(swap[curr][j], 1 + keep[prev])
                if j > 0:
                    swap[curr][j] = min(swap[curr][j], 1 + swap[prev][j - 1])

        res = min(keep[curr], swap[curr][m - 1])
        return res if res < math.inf else -1
