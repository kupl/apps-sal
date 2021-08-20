class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        res = [1] * n
        for (a, i) in sorted(([a, i] for (i, a) in enumerate(arr))):
            for di in [-1, 1]:
                for j in range(i + di, i + d * di + di, di):
                    if not (0 <= j < n and arr[j] < arr[i]):
                        break
                    res[i] = max(res[j] + 1, res[i])
        return max(res)
