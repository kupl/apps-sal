class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        # Maintain two dp array: 1 for keep arr1[i], 1 for swap arr1[i] with arr2[j]
        # Convert arr2 to sorted unique set
        a = arr1
        b = sorted(list(set(arr2)))
        n, m = len(a), len(b)
        keep = [0, math.inf]  # keep[i] = keep a[i]
        swap = [[1] * m, [math.inf] * m]  # swap[i][j] = a[i] replaced with b[j]

        prev, curr = 1, 0
        for i in range(1, n):
            prev, curr = curr, prev
            # must init every time
            swap[curr] = [math.inf] * m
            keep[curr] = math.inf
            # keep[i] case 1: a[i] is bigger than previous keep[i-1]
            if a[i] > a[i - 1]:
                keep[curr] = keep[prev]
            for j in range(m):
                # keep[i] case 2: a[i] is bigger then previous swap value.
                if a[i] > b[j]:
                    keep[curr] = min(keep[curr], swap[prev][j])
                # swap case 1: when a[i-1] keeps
                if b[j] > a[i - 1]:
                    swap[curr][j] = min(swap[curr][j], 1 + keep[prev])
                # Swap case 2: when a[i-1] swapped
                if j > 0:
                    # only need to check last swap[i-1][j-1] since swap[][j] decreases when j increases.
                    swap[curr][j] = min(swap[curr][j], 1 + swap[prev][j - 1])

        res = min(keep[curr], swap[curr][m - 1])
        return res if res < math.inf else -1
