class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        ans = -1
        size = collections.Counter()
        comp = [0 for _ in range(len(arr) + 2)]
        for i, n in enumerate(arr):
            left, right = comp[n - 1], comp[n + 1]
            comp[n] = comp[n - left] = comp[n + right] = left + right + 1
            size[left] -= 1
            size[right] -= 1
            size[comp[n]] += 1
            if size[m] > 0:
                ans = i + 1
        return ans
