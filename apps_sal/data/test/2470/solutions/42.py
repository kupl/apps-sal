class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        # Maintain two dp array: 1 for keep arr1[i], 1 for swap arr1[i] with arr2[j]
        # Convert arr2 to sorted unique set
        a = arr1
        b = sorted(list(set(arr2)))
        n, m = len(a), len(b)
        keep = [math.inf] * n  # keep[i] = keep a[i]
        swap = [[math.inf] * m for _ in range(n)]  # swap[i][j] = a[i] replaced with b[j]
        # init
        keep[0] = 0  # keep a[0], no swap
        swap[0] = [1] * m  # can be swapped with any a[j]

        for i in range(1, n):
            # keep[i] case 1: a[i] is bigger than previous keep[i-1]
            if a[i] > a[i - 1]:
                keep[i] = keep[i - 1]
            for j in range(m):
                # keep[i] case 2: a[i] is bigger then previous swap value.
                if a[i] > b[j]:
                    keep[i] = min(keep[i], swap[i - 1][j])
                # swap case 1: when a[i-1] keeps
                if b[j] > a[i - 1]:
                    swap[i][j] = min(swap[i][j], 1 + keep[i - 1])
                # Swap case 2: when a[i-1] swapped
                if j > 0:
                    # only need to check last swap[i-1][j-1] since swap[][j] decreases when j increases.
                    swap[i][j] = min(swap[i][j], 1 + swap[i - 1][j - 1])

        res = min(keep[n - 1], swap[n - 1][m - 1])
        return res if res < math.inf else -1        
