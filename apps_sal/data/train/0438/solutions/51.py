class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        ans = -1
        comps = [0 for _ in range(len(arr) + 2)]
        size = collections.Counter()
        for i, a in enumerate(arr):
            l, r = comps[a - 1], comps[a + 1]
            comps[a] = comps[a - l] = comps[a + r] = l + r + 1
            size[l] -= 1
            size[r] -= 1
            size[comps[a]] += 1
            if size[m] > 0:
                ans = i + 1
        return ans
