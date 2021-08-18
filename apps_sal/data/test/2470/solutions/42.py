class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        a = arr1
        b = sorted(list(set(arr2)))
        n, m = len(a), len(b)
        keep = [math.inf] * n
        swap = [[math.inf] * m for _ in range(n)]
        keep[0] = 0
        swap[0] = [1] * m

        for i in range(1, n):
            if a[i] > a[i - 1]:
                keep[i] = keep[i - 1]
            for j in range(m):
                if a[i] > b[j]:
                    keep[i] = min(keep[i], swap[i - 1][j])
                if b[j] > a[i - 1]:
                    swap[i][j] = min(swap[i][j], 1 + keep[i - 1])
                if j > 0:
                    swap[i][j] = min(swap[i][j], 1 + swap[i - 1][j - 1])

        res = min(keep[n - 1], swap[n - 1][m - 1])
        return res if res < math.inf else -1
