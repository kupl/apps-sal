class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # top-down dp
        res = [1] * len(arr)
        for a, i in sorted([a, i] for i, a in enumerate(arr)):
            for di in [-1, 1]:
                for j in range(i + di, i + d * di + di, di):
                    if not (0 <= j < len(arr) and arr[j] < arr[i]):
                        break
                    res[i] = max(res[i], 1 + res[j])
        return max(res)
